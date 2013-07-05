%define gname	etracer
%define beta	beta1

Name:		extremetuxracer
Version:	0.6
Release:	0.%beta.1
Summary:	OpenGL racing game featuring Tux
License:	GPLv2
Group:		Games/Arcade
URL:		http://extremetuxracer.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/extremetuxracer/%{name}-%{version}beta.tar.gz
# Current code is available in svn only
# svn co svn://svn.code.sf.net/p/extremetuxracer/code/tags/"0.6 Beta 1"
Source0:	extremetuxracer-%version-%beta.tar.xz
Requires:	squirrel
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glu)
BuildRequires:	texinfo
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	squirrel
BuildRequires:	pkgconfig(squirrel)

Provides:	tuxracer = %{version}-%{release}

%description
Extreme Tux Racer is an OpenGL racing game featuring Tux, the Linux
mascot. The goal of the game is to slide down a snow- and ice-covered
mountain as quickly as possible.  It is based on the GPL version of
TuxRacer.

%prep
%setup -q -n %{name}-%{version}-%{beta}

%build
aclocal
autoheader
automake -a --foreign
autoconf
CFLAGS="%{optflags} -O3 -ffast-math" \
CXXFLAGS="%{optflags} -O3 -ffast-math" \
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--disable-debug
%make

%install
%makeinstall_std

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Extreme Tux Racer
Comment=OpenGL racing game featuring Tux
Exec=%{_gamesbindir}/etr
Icon=%{gname}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

for r in 16 22 32 48; do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps
	convert resources/%{gname}icon.svg -scale ${r}x${r} %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/%{gname}.png
done
install -D resources/%{gname}icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{gname}.svg

%find_lang %{gname} || touch %{gname}.lang

cat > README.urpmi << EOF

---------------------------Description-------------------------------------

Extreme Tux Racer is an OpenGL racing game featuring Tux, 
the Linux mascot. The goal of the game is to slide down 
a snow- and ice-covered mountain as quickly as possible. 
It is based on the GPL version of TuxRacer.

-----------------------------Warning--------------------------------------- 

It might occur that etracer won't start,
in that case you need to edit ~/.ppracer/options
and adjust values to your hardware configuration.

---------------------------DescriptionFR-----------------------------------
Extreme Tux Racer est un jeu OpenGL avec en hero Tux la 
masctotte Linux. Le but de ce jeu est de faire descendre Tux 
le plus rapidement possible de pistes pentues et recouvertes de neige et
de glace.
Ce jeu est bas? sur la version GPL de TuxRacer.

-----------------------------Attention-------------------------------------

Il est possible que etracer ne demarre pas.
Dans ce cas il vous faudra editer le fichier ~/.ppracer/options
et changer les valeurs pour qu elles soient correctes avec votre
configuration materielle.

---------------------------------------------------------------------------
EOF

%files -f %{gname}.lang
%defattr(644,root,root,755)
%doc README.urpmi
%{_gamesdatadir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{gname}.*
%attr(755,root,root) %{_gamesbindir}/etr

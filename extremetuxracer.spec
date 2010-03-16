%define gname	etracer
%define	name	extremetuxracer
%define	Summary	OpenGL racing game featuring Tux

Name:		extremetuxracer
Version:	0.5
Release:	%mkrel 0.beta.4
Summary:	%{Summary}
License:	GPLv2
Group:		Games/Arcade
URL:		http://www.extremetuxracer.com/
Source0:	http://downloads.sourceforge.net/extremetuxracer/%{name}-%{version}beta.tar.gz
Patch0:		extremetuxracer-0.5-defaultopt.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	squirrel
BuildRequires:	SDL_mixer-devel
BuildRequires:	X11-static-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	esound-devel
BuildRequires:	MesaGLU-devel
BuildRequires:	texinfo
BuildRequires:	libpng-devel
BuildRequires:	freetype-devel
BuildRequires:	libxslt-devel
BuildRequires:	libxml2 >= 2.4.11
BuildRequires:	squirrel
BuildRequires:	tcl-devel
BuildRequires:	libsquirrel-devel

Obsoletes:	tuxracer
Provides:	tuxracer

Obsoletes:	ppracer
Provides:	ppracer

Obsoletes:	wherever-racer
Provides:	wherever-racer

%description
Extreme Tux Racer is an OpenGL racing game featuring Tux, the Linux
mascot. The goal of the game is to slide down a snow- and ice-covered
mountain as quickly as possible.  It is based on the GPL version of
TuxRacer.

%prep
%setup -q -n extreme-tuxracer-%{version}beta
%patch0 -p1 -b .defaultopt
unzip %{gname}icons.zip

%build
CFLAGS="%{optflags} -O3 -ffast-math" \
CXXFLAGS="%{optflags} -O3 -ffast-math" \
%configure2_5x	--bindir=%{_gamesbindir} \
		--with-data-dir=%{_gamesdatadir}/%{name}\
		--datadir=%{_gamesdatadir} \
		--disable-debug
%make

%install
rm -rf %{buildroot} %{gname}.lang
%{makeinstall_std}

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Extreme Tux Racer
Comment=%{Summary}
Exec=%{_gamesbindir}/%{gname}
Icon=%{gname}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

for r in 16 22 32 48; do
    install -D %{gname}icons/%{gname}icon_${r}.png %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/%{gname}.png
done
install -D %{gname}icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{gname}.svg

%find_lang %{gname}

cat > README.urpmi << EOF

---------------------------Description-------------------------------------

Extreme Tux Racer is an OpenGL racing game featuring Tux, 
the Linux mascot. The goal of the game is to slide down 
a snow- and ice-covered mountain as quickly as possible. 
It is based on the GPL version of TuxRacer.

-----------------------------Warning--------------------------------------- 

It might occurs that etracer won t start, 
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

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{gname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.urpmi
%{_gamesdatadir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{gname}.svg
%{_datadir}/icons/hicolor/*/apps/%{gname}.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{gname}


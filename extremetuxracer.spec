%define gname	etracer
#define beta	%{nil}

Name:		extremetuxracer
Version:	0.7.5
Release:	%{?beta:0.%beta.}2
Summary:	OpenGL racing game featuring Tux
License:	GPLv2
Group:		Games/Arcade
URL:		http://extremetuxracer.sourceforge.net/
# Current code is available in svn only
# svn co svn://svn.code.sf.net/p/extremetuxracer/code/tags/"0.6 Beta 1"
%if 0%{?beta:1}
Source0:	extremetuxracer-%version-%beta.tar.xz
%else
Source0:	http://sourceforge.net/projects/extremetuxracer/files/releases/%version/etr-%version.tar.xz
%endif
Patch1:		etr-0.7.4-ptr.patch
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glu)
BuildRequires:	texinfo
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sfml-system)
BuildRequires:	imagemagick

Provides:	tuxracer = %{version}-%{release}

%description
Extreme Tux Racer is an OpenGL racing game featuring Tux, the Linux
mascot. The goal of the game is to slide down a snow- and ice-covered
mountain as quickly as possible.  It is based on the GPL version of
TuxRacer.

%prep
%setup -q -n etr-%{version}
%apply_patches

%build
CFLAGS="%{optflags} -Ofast -ffast-math" \
CXXFLAGS="%{optflags} -Ofast -ffast-math" \
%configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--disable-debug
%make

%install
%makeinstall_std

for r in 16 22 32 48; do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps
	convert resources/etr.svg -scale ${r}x${r} %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/%{gname}.png
done
install -D resources/etr.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{gname}.svg

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

%files
%defattr(644,root,root,755)
%doc README.urpmi
%doc %{_docdir}/etr
%{_gamesdatadir}/*
%{_datadir}/applications/etr.desktop
%{_datadir}/appdata/etr.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{gname}.*
%{_datadir}/pixmaps/etr.png
%{_datadir}/pixmaps/etr.svg
%attr(755,root,root) %{_gamesbindir}/etr

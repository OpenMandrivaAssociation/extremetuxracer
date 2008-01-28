%define	name	ppracer
%define	version	0.5
%define	aversion 0.5alpha
%define	release	%mkrel 0.alpha4
%define	Summary	PlanetPenguin Racer is an OpenGL racing game

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		Games/Arcade
URL:		http://projects.planetpenguin.de/racer/
Source0:	http://download.berlios.de/ppracer/%{name}-%{aversion}.tar.bz2
Source1:	%{name}-link.tar.bz2
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
Patch0:		ppracer-squirrel.h.patch.bz2
Patch1:		ppracer-0.5alpha-gcc4.1-fix.patch
Buildroot:	%{_tmppath}/%{name}-%{aversion}-%{release}-buildroot
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
BuildRequires:	libsquirrel-devel

Obsoletes:	tuxracer
Provides:	tuxracer

%description
PlanetPenguin Racer is an OpenGL racing game featuring Tux,
the Linux mascot. The goal of the game is to slide down a snow-
and ice-covered mountain as quickly as possible.
It is based on the GPL version of TuxRacer.

%prep
%setup -q -n %{name}-%{aversion}

%ifarch amd64 x86_64
%patch0 -p0
%endif
%patch1 -p1 -b .gcc41

%build
%configure	--bindir=%{_gamesbindir} \
		--with-data-dir=%{_gamesdatadir}/%{name}\
		--datadir=%{_gamesdatadir} \
		--disable-debug
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}



install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Planet Penguin Racer
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

cat > README.urpmi << EOF

---------------------------Description-------------------------------------

PlanetPenguin Racer is an OpenGL racing game featuring Tux, 
the Linux mascot. The goal of the game is to slide down 
a snow- and ice-covered mountain as quickly as possible. 
It is based on the GPL version of TuxRacer.

-----------------------------Warning--------------------------------------- 

It might occurs that ppracer won t start, 
in that case you need to edit ~/.ppracer/options 
and adjust values to your hardware configuration.

---------------------------DescriptionFR-----------------------------------
PlanetPenguin Racer est un jeu OpenGL avec en hero Tux la 
masctotte Linux. Le but de ce jeu est de faire descendre Tux 
le plus rapidement possible de pistes pentues et recouvertes de neige et
de glace.
Ce jeu est bas? sur la version GPL de TuxRacer.

-----------------------------Attention-------------------------------------

Il est possible que ppracer ne demarre pas.
Dans ce cas il vous faudra editer le fichier ~/.ppracer/options
et changer les valeurs pour qu elles soient correctes avec votre
configuration materielle.

---------------------------------------------------------------------------
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.urpmi
%{_gamesdatadir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}*.png
%{_miconsdir}/%{name}*.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}

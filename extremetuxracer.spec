%define	name	extremetuxracer
%define	version	0.4
%define	release	%mkrel 1
%define	Summary	Extreme Tux Racer OpenGL racing game

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		Games/Arcade
URL:		http://www.extremetuxracer.com/
Source0:	http://downloads.sourceforge.net/extremetuxracer/%{name}-%{version}.tar.gz
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
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
BuildRequires:	libsquirrel-devel

Obsoletes:	tuxracer
Provides:	tuxracer

%description
Extreme Tux Racer is an OpenGL racing game featuring Tux,
the Linux mascot. The goal of the game is to slide down a snow-
and ice-covered mountain as quickly as possible.
It is based on the GPL version of TuxRacer.

%prep
%setup -q

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

Extreme Tux Racer is an OpenGL racing game featuring Tux, 
the Linux mascot. The goal of the game is to slide down 
a snow- and ice-covered mountain as quickly as possible. 
It is based on the GPL version of TuxRacer.

-----------------------------Warning--------------------------------------- 

It might occurs that ppracer won t start, 
in that case you need to edit ~/.ppracer/options 
and adjust values to your hardware configuration.

---------------------------DescriptionFR-----------------------------------
Extreme Tux Racer est un jeu OpenGL avec en hero Tux la 
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

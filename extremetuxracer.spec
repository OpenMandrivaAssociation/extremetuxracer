%define	name	extremetuxracer
%define	gname	etracer
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
unzip %{gname}icons.zip

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
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.urpmi
%{_gamesdatadir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{gname}.svg
%{_datadir}/icons/hicolor/*/apps/%{gname}.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{gname}

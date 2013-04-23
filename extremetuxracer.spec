%define gname	etracer

Name:		extremetuxracer
Version:	0.5
Release:	0.beta.8
Summary:	OpenGL racing game featuring Tux
License:	GPLv2
Group:		Games/Arcade
URL:		http://www.extremetuxracer.com/
Source0:	http://downloads.sourceforge.net/extremetuxracer/%{name}-%{version}beta.tar.gz
Patch0:		extremetuxracer-0.5-defaultopt.patch
Patch1:		extremetuxracer-0.5-link.patch
Patch2:		extremetuxracer-0.5-install.patch
Patch3:		extreme-tuxracer-0.5beta-libpng15.patch
Patch4:		extreme-tuxracer-0.5beta-automake113.patch
Requires:	squirrel
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(glu)
BuildRequires:	texinfo
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	squirrel
BuildRequires:	tcl-devel
BuildRequires:	libsquirrel-devel

Provides:	tuxracer = %{version}-%{release}

%description
Extreme Tux Racer is an OpenGL racing game featuring Tux, the Linux
mascot. The goal of the game is to slide down a snow- and ice-covered
mountain as quickly as possible.  It is based on the GPL version of
TuxRacer.

%prep
%setup -q -n extreme-tuxracer-%{version}beta
%patch0 -p1 -b .defaultopt
%patch1 -p0 -b .link
%patch2 -p0 -b .install
%patch3 -p1 -b .libpng
%patch4 -p1 -b .automake113
unzip %{gname}icons.zip

%build
autoreconf -fi
CFLAGS="%{optflags} -O3 -ffast-math" \
CXXFLAGS="%{optflags} -O3 -ffast-math" \
%configure2_5x	--bindir=%{_gamesbindir} \
		--with-data-dir=%{_gamesdatadir}/%{name}\
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

%files -f %{gname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.urpmi
%{_gamesdatadir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{gname}.*
%attr(755,root,root) %{_gamesbindir}/%{gname}



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.beta.6mdv2011.0
+ Revision: 664166
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.beta.5mdv2011.0
+ Revision: 605115
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.beta.4mdv2010.1
+ Revision: 522580
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5-0.beta.3mdv2010.0
+ Revision: 424395
- rebuild

* Mon Mar 16 2009 Giuseppe Ghibò <ghibo@mandriva.com> 0.5-0.beta.2mdv2009.1
+ Revision: 355692
- Default windowed resolution to 800x600 (640x480 would leave out some element).

* Sun Mar 15 2009 Giuseppe Ghibò <ghibo@mandriva.com> 0.5-0.beta.1mdv2009.1
+ Revision: 355192
- Release 0.5beta.
- Better optimization.
- Default to windowed and show FPS (Patch0).
- Added languages.

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 0.4-4mdv2009.1
+ Revision: 311014
- re-add gname define (got lost somehow)
- obsolete wherever-racer, which appears to be dead now
- rebuild for new tcl

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.4-3mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Jan 28 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.4-3mdv2008.1
+ Revision: 159485
- fix executable name in README.urpmi (s/ppracer/etracer/)

* Mon Jan 28 2008 Olivier Blin <oblin@mandriva.com> 0.4-2mdv2008.1
+ Revision: 159157
- nicer summary (from tpg)

* Mon Jan 28 2008 Olivier Blin <oblin@mandriva.com> 0.4-1mdv2008.1
+ Revision: 159113
- buildrequire tcl-devel
- obsoletes/provides ppracer
- use icons from source and install them in XDG locations
- adapt to new etracer binary name
- drop unnecessary build patches
- drop unused source
- extremetuxracer 0.4
- rename ppracer as extremetuxracer
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.alpha4mdv2008.0
+ Revision: 74800
- Import ppracer


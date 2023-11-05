%define debug_package %{nil}
%global optflags %optflags -Ofast
#define beta %{nil}

Name:		extremetuxracer
Version:	0.8.3
Release:	%{?beta:0.%beta.}1
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
%autosetup -n etr-%{version} -p1

%build
%configure \
	--bindir=%{_bindir} \
	--datadir=%{_datadir}

%make_build

%install
%make_install

for r in 16 22 32 48; do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps
	convert resources/etr.svg -scale ${r}x${r} %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/etr.png
done
install -D resources/etr.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/etr.svg

# Workaround for "/usr/bin/debugedit: Cannot handle 8-byte build ID"
strip -R .comment --strip-unneeded %{buildroot}%{_bindir}/etr

%files
%defattr(644,root,root,755)
%doc %{_docdir}/etr
%{_datadir}/etr/
%{_datadir}/applications/net.sourceforge.extremetuxracer.desktop
%{_datadir}/metainfo/net.sourceforge.extremetuxracer.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/etr.*
%{_datadir}/pixmaps/etr.png
%{_datadir}/pixmaps/etr.svg
%attr(755,root,root) %{_bindir}/etr

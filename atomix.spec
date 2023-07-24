Summary:	Little game where you have to build molecules out of single atoms
Summary(pl.UTF-8):	Mała gra, w której trzeba budować cząsteczki z pojedynczych atomów
Name:		atomix
Version:	44.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/atomix/44/%{name}-%{version}.tar.xz
# Source0-md5:	448892592ab039fcff4ce90336f50a06
URL:		https://wiki.gnome.org/Apps/Atomix
BuildRequires:	gdk-pixbuf2-devel >= 2.0.5
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	libgnome-games-support-devel >= 1
BuildRequires:	meson >= 0.41
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atomix is a little game where you have to build molecules out of
single atoms. These are laying around between the walls and obstacles
on the playfield. Once you have pushed an atom in one direction it
moves until it hits an obstacle or another atom. The game is inspired
by the original Amiga version.

%description -l pl.UTF-8
Atomix jest małą grą, w której trzeba budować cząsteczki z
pojedynczych atomów, leżących dookoła na planszy. Gdy atom zostanie
popchnięty, porusza się w zadanym kierunku aż do momentu uderzenia w
inny atom lub przeszkodę. Inspiracją do powstania tej gry była
oryginalna wersja na Amigę.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README.md
%attr(755,root,root) %{_bindir}/atomix
%{_datadir}/atomix
%{_datadir}/metainfo/atomix.appdata.xml
%{_desktopdir}/atomix.desktop
%{_iconsdir}/hicolor/*x*/apps/atomix.png
%{_iconsdir}/hicolor/symbolic/apps/atomix-symbolic.svg

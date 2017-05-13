Summary:	Little game where you have to build molecules out of single atoms
Summary(pl.UTF-8):	Mała gra, w której trzeba budować cząsteczki z pojedynczych atomów
Name:		atomix
Version:	3.22.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/atomix/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	027372b149248de71adc3a48d2943f99
URL:		https://wiki.gnome.org/Apps/Atomix
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	gdk-pixbuf2-devel >= 2.0.5
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
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
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/atomix
%{_datadir}/appdata/atomix.appdata.xml
%{_datadir}/atomix
%{_desktopdir}/atomix.desktop
%{_iconsdir}/hicolor/*x*/apps/atomix.png
%{_iconsdir}/hicolor/symbolic/apps/atomix-symbolic.svg

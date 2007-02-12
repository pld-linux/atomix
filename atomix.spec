Summary:	Little game where you have to build molecules out of single atoms
Summary(pl.UTF-8):   Mała gra w której trzeba budować cząsteczki z pojedynczych atomów
Name:		atomix
Version:	1.0.1
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://triq.net/~jens/download/%{name}-%{version}.tar.gz
# Source0-md5:	dd0d5d29020863d8140f919edd96d150
Patch0:		%{name}-desktop.patch
URL:		http://triq.net/~jens/atomix.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	pkgconfig
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
%patch0 -p1

# Note: it is also for desktop translation
mv -f po/{no,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_localstatedir}/games/%{name}.scores

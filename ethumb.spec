Summary:	Enlightenment Foundation Library
Name:		ethumb
Version:	1.7.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	30fa1b67d5cd94a0ab99973363a77d1c
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e_dbus-devel
BuildRequires:	edje-devel
BuildRequires:	emotion-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thumbnail generation library.

%package devel
Summary:	Header files for ethumb library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for ethumb library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-epdf			\
	--disable-install-examples	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ethumb
%attr(755,root,root) %ghost %{_libdir}/libethumb.so.1
%attr(755,root,root) %{_libdir}/libethumb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libethumb.so
%{_includedir}/ethumb-1
%{_pkgconfigdir}/ethumb.pc


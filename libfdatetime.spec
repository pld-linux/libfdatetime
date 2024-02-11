# m4/libcerror.m4
%define		libcerror_ver	20120425
Summary:	Library to support various date and time formats that are used in file formats
Summary(pl.UTF-8):	Biblioteka obsługująca różne formaty daty i czasu używane w formatach plików
Name:		libfdatetime
Version:	20240115
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libfdatetime/releases
Source0:	https://github.com/libyal/libfdatetime/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	b1b1891e712a139e7682031535c937aa
URL:		https://github.com/libyal/libfdatetime/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfdatetime is a library to support various date and time formats
that are used in file formats.

%description -l pl.UTF-8
libfdatetime to biblioteka obsługująca różne formaty daty i czasu
używane w formatach plików.

%package devel
Summary:	Header files for libfdatetime library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfdatetime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}

%description devel
Header files for libfdatetime library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfdatetime.

%package static
Summary:	Static libfdatetime library
Summary(pl.UTF-8):	Statyczna biblioteka libfdatetime
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfdatetime library.

%description static -l pl.UTF-8
Statyczna biblioteka libfdatetime.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfdatetime.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libfdatetime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfdatetime.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfdatetime.so
%{_includedir}/libfdatetime
%{_includedir}/libfdatetime.h
%{_pkgconfigdir}/libfdatetime.pc
%{_mandir}/man3/libfdatetime.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfdatetime.a

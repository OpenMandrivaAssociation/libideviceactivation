%define major	2
%define api	1.0

%define oldlibname %mklibname ideviceactivation %{api} %{major}
%define libname %mklibname ideviceactivation %{api}
%define devname %mklibname -d ideviceactivation

%define	git	20230802

Summary:	Library to manage the activation of iOS device
Name:		libideviceactivation
Version:	1.1.2
Release:	%{?git:0.%{git}.}2
Group:		System/Libraries
License:	LGPLv2+
Url:		https://www.libimobiledevice.org/
%if 0%{?git:1}
Source0:	https://github.com/libimobiledevice/libideviceactivation/archive/refs/heads/master.tar.gz#/%{name}-%{git}.tar.gz
%else
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz
%endif

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	pkgconfig(libimobiledevice-1.0)
BuildRequires:	pkgconfig(libimobiledevice-glue-1.0)
BuildRequires:	pkgconfig(libplist-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)

%description
Provides an interface to activate and deactivate iOS devices by
talking to Apple's webservice. 
A command-line utility ideviceactivation is also available


%package -n %{libname}
Group:		System/Libraries
Summary:	Library to manage the activation of iOS devices
Suggests:	%{name} >= %{version}-%{release}

%description -n %{libname}
Library to manage the activation of iOS devices

%package -n %{devname}
Summary:	Development package for libirecovery
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name}, development headers and libraries.


%package -n ideviceactivation
Group:          System/Tools
Summary:        Tool to access iboot/iBSS over usb on IOS devices
Requires:       %{libname} = %{version}-%{release}

%description -n ideviceactivation
ideviceactivation is a system tool which can be used to activate or deactivate iOS devices

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
autoreconf -fiv

%configure \
	--disable-static

%build
%make_build

%install
%make_install

%files 
%doc NEWS README.md COPYING

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}-%{api}.so

%files -n ideviceactivation
%{_bindir}/ideviceactivation
%{_mandir}/man1/*


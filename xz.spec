Name:           xz
Version:        5.2.4
Release:        5
Summary:        A free general-purpose data compreession software with LZMA2 algorithm
License:        Public Domain, LGPLv2.1 and GPLv2+
URL:            http://tukaani.org/xz
Source0:        http://tukaani.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  perl-interpreter

Requires:       %{name} = %{version}-%{release}
Requires:       grep >= 2.20-5
Provides:       xz-libs
Obsoletes:      xz-libs
Obsoletes:      %{name}-compat-libs < %{version}-%{release}

%description
XZ Utils is free general-purpose data compression software with a high compression ratio.
XZ Utils were written for POSIX-like systems, but also work on some not-so-POSIX systems. XZ Utils are the successor to LZMA Utils.

The core of the XZ Utils compression code is based on LZMA SDK, but it has been modified quite a lot to be suitable for XZ Utils.
The primary compression algorithm is currently LZMA2, which is used inside the .xz container format. With typical files, XZ Utils create 30% smaller output than gzip and 15% smaller output than bzip2.

%package        devel
Summary:        Libraries & headers for xz
Requires:       %{name} = %{version}-%{release}
Provides:       lzma = %{version}
Provides:       xz-static xz-lzma-compat
Obsoletes:      lzma < %{version}
Obsoletes:      xz-static xz-lzma-compat

%description    devel
This package mainly includes the following contents: static library,
the header file, example, tests use case, other development and use of content.

%package        help
Summary:        Help documentation related to xz
BuildArch:      noarch

%description    help
This package includes help documentation and manuals related to xz.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

%find_lang %name

%check
LD_LIBRARY_PATH=$PWD/src/liblzma/.libs make check

%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_pkgdocdir}
%license %{_pkgdocdir}/COPYING*
%{_bindir}/*xz*
%{_bindir}/*lz*

%{_libdir}/lib*.so.5*
%exclude %_pkgdocdir/examples*
%exclude %{_libdir}/*.la

%files devel
%dir %{_includedir}/lzma
%doc %_pkgdocdir/examples*
%{_includedir}/lzma/*.h
%{_includedir}/lzma.h

%{_libdir}/pkgconfig/liblzma.pc
%{_libdir}/liblzma.a
%{_libdir}/*.so

%files help
%{_mandir}/man1/*lz*
%{_mandir}/man1/*xz*

%changelog
* Sat Jan 18 2020 JeanLeo<liujianliu.liu@huawei.com> - 5.2.4-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:remove useless file or patch

* Mon Sep 2 2019 dongjian<dongjian13@huawei.com> - 5.2.4-4
- Rebuild the xz and fix description

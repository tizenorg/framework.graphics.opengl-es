#sbs-git:slp/pkgs/o/opengl-es opengl-es 0.1.1 0d774b1127022844afc7e7eb99b76bedb95f8fe9
%ifarch %{ix86}
%define PKGPATH "pkgconfig_i686"
%else
%define PKGPATH "pkgconfig_arm"
%endif

Name:       opengl-es
Summary:    metapackage for the OpenGL ES library
Version:    0.1.3
Release:    4
Group:      libs
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Requires:   opengl-es-drv
ExcludeArch: %{arm}

%description
metapackage for the OpenGL ES library
 This is a meta package that will point to the latest OpenGL ES driver.
 .
 It does not provide any drivers itself..

%package devel
Summary:    metapackage for development files of the OpenGL ES library
Group:      libs
Requires:   %{name} = %{version}-%{release}
Requires:   opengl-es-drv-devel

%description devel
metapackage for development files of the OpenGL ES library
 This is a meta package that will point to the latest development libraries,
 header files needed by programs that want to compile with OpenGL ES.
 .
 It does not provide any development files itself..



%prep
%setup -q


%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -a ./%{PKGPATH}/*.pc %{buildroot}%{_libdir}/pkgconfig/


%files
%manifest opengl-es.manifest
%defattr(-,root,root,-)

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/opengl-es-11.pc
%{_libdir}/pkgconfig/opengl-es-20.pc

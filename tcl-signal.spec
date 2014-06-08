Name:           tcl-signal
Version:        1.4
Release:        8%{?dist}
Summary:        This extension adds dynamically loadable signal handling to Tcl/Tk scripts

Group:          System Environment/Libraries
License:        MIT
URL:            http://www.nyx.net/~mschwart/signal_ext.html
Source0:        http://www.nyx.net/~mschwart/signal_ext1.4.tar.gz
#Strip off trailing entries in TCL_PACKAGE_PATH
Patch0:         signal_ext-tclpath.patch
#Add DESTDIR support
Patch1:         signal_ext-destdir.patch
#Add lib64 support
Patch2:         signal_ext-lib64.patch
#Rename library to libtclsignal.so
Patch3:         signal_ext-libtclsignal.patch

BuildRequires:  tcl-devel


%description
This extension adds dynamically loadable signal handling to Tcl/Tk scripts.

Note that the library has been renamed to libtclsignal-%{version}.so for ease in
linking and to prevent conflicts.


%prep
%setup -q -n signal_ext%{version}
%patch0 -p1 -b .tclpath
%patch1 -p1 -b .destdir
%patch2 -p1 -b .lib64
%patch3 -p1 -b .libtclsignal


%build
export TCL_INC_DIR=%{_includedir}
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
sed -i -e s,signal.so,%{_libdir}/libtclsignal-%{version}.so, $RPM_BUILD_ROOT%{_libdir}/tcl*/signal/pkgIndex.tcl
chmod 644 $RPM_BUILD_ROOT%{_libdir}/tcl*/signal/pkgIndex.tcl


%files
%doc README sig.announce.1.4
%{_libdir}/libtclsignal-%{version}.so
%{_libdir}/tcl*/signal


%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 4 2012 Orion Poplawski <orion@cora.nwra.com> 1.4-4
- Fix library name in description

* Mon Aug 27 2012 Orion Poplawski <orion@cora.nwra.com> 1.4-3
- Use spaces
- Drop BuildRoot, clean
- Add version to libtclsignal

* Thu May 5 2011 Orion Poplawski <orion@cora.nwra.com> 1.4-2
- Rename to tcl-signal
- Rename library and move to %%{_libdir}

* Wed May 4 2011 Orion Poplawski <orion@cora.nwra.com> 1.4-1
- Initial package

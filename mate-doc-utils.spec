Summary:	MATE XML documentation utilities
Name:		mate-doc-utils
Version:	1.4.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{lua: print (string.match(rpm.expand("%{version}"),"%d+.%d+"))}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	docbook-dtd44-xml
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	libxml2-utils
BuildRequires:	xsltproc
BuildRequires:	python-libxml2
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(rarian)

Requires:	xsltproc

%description
mate-doc-utils is a collection of documentation utilities for the MATE
project. Notably, it contains utilities for building documentation and all
auxiliary files in your source tree, and it contains the DocBook XSLT.

%package xml2po
Summary:	Tool to extract translatable content from XML documents
Requires: 	python-libxml2

%description xml2po
xml2po is a simple Python program which extracts translatable
content from free-form XML documents and outputs gettext compatible
POT files.

%package devel
Summary:	A Collection of Documentation Utilities for MATE
Group:		Development/GNOME and GTK+ 
Requires:	%{name} = %{version}
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd44-xml
Requires:	libxml2-utils
Requires:	mate-doc-utils-xml2po

%description devel
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--build=%{_build} \
	--disable-scrollkeeper \
	--enable-documentation

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/mate-doc-tool
%dir %{_datadir}/mate-doc-utils
%{_datadir}/mate-doc-utils/icons
%{_datadir}/mate-doc-utils/watermarks
%dir %{_datadir}/xml/
%{_datadir}/xml/mate

%files xml2po
%doc xml2po/AUTHORS xml2po/ChangeLog xml2po/COPYING xml2po/NEWS xml2po/README
%{_bindir}/xml2po
%{py_puresitedir}/xml2po/
%{_mandir}/man1/xml2po.1*

%files devel
%{_bindir}/mate-doc-prepare
%{_datadir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_datadir}/mate-doc-utils/mate-debian.sh
%{_datadir}/mate-doc-utils/mate-doc-utils.make
%{_datadir}/mate-doc-utils/templates
%{_datadir}/mate-doc-utils/template*.*
# this conflicts with gnome-doc-utils
%{_datadir}/xml/mallard



%changelog
* Fri Jul 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811303
- new version 1.4.0

* Sat Jun 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.1-3
+ Revision: 804180
- rebuild moved conflicting files with gnome-doc-utils to the dev pkg

* Fri Jun 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.1-2
+ Revision: 803384
- bump release
- rebuild splitting out xml2po and devel pkgs
- the xml2po pkg is still gonna conflict with the gnome-doc-utils one
- but atleast mate-doc-utils and gnome-doc-utils should not conflict

* Mon Apr 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2.1-1
+ Revision: 793006
- imported package mate-doc-utils


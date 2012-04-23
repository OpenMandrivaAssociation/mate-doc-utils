Name:		mate-doc-utils
Summary:	MATE XML documentation utilities
Version:	1.2.1
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(rarian)
BuildRequires:	mate-common
BuildRequires:	intltool >= 0.25
BuildRequires:	xsltproc
BuildRequires:	python-libxml2
BuildRequires:	libxml2-utils
Requires:	libxml2-utils
Requires:	python-libxml2
BuildArch:	noarch

%description
mate-doc-utils is a collection of documentation utilities for the MATE
project. Notably, it contains utilities for building documentation and all
auxiliary files in your source tree, and it contains the DocBook XSLT.

%prep
%setup -q

%build
./autogen.sh \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--localstatedir=%{_localstatedir} \
	--disable-scrollkeeper
%make

%install
%makeinstall_std
%__mv %{buildroot}%{_datadir}/%{name}/icons/ %{buildroot}%{_iconsdir}
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/mate-*
%{_bindir}/xml2po
%{_datadir}/mate/help/
%{_datadir}/pkgconfig/*.pc
%{_datadir}/xml/mallard/1.0/mallard.rn?
%{_datadir}/xml/mate/
%{py_sitedir}/xml2po/
%{_datadir}/aclocal/mate-doc-utils.m4
%{_mandir}/man1/xml2po.1*
%{_iconsdir}/hicolor/*/status/admon-*
%{_datadir}/mate-doc-utils/
%{_datadir}/omf/mate-doc-*/

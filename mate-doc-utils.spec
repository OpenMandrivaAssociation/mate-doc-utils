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
Requires:	python-libxml2
Requires:	libxml2-utils
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

%files
%{_bindir}/mate-*
%{_datadir}/mate/help/
%{_datadir}/omf/mate-doc-make/mate-doc-make-C.omf
%{_datadir}/pkgconfig/*.pc
%{_datadir}/xml/mallard/1.0/mallard.rn?
%{_datadir}/xml/mate/

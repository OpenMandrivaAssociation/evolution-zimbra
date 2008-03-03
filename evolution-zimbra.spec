%define evo_version 2.21.1
%define eds_version 2.21.1
%define glib_version 2.8.1

%define evo_api_version 2.22
%define eds_api_version 1.2

### Abstract ###

Name: evolution-zimbra
Version: 0.1.0
Release: %mkrel 1
License: Public Domain
Group: System Environment/Libraries
Summary: Zimbra Connector for Evolution
URL: http://sourceforge.net/projects/zimbraevo/
Source: http://ovh.dl.sourceforge.net/sourceforge/zimbraevo/evolution-zimbra-0.1.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel
BuildRequires: evolution-devel 
#>= %{evo_version}
BuildRequires: evolution-data-server-devel 
#>= %{eds_version}
BuildRequires: gettext
BuildRequires: glib2-devel 
#>= %{glib_version}
BuildRequires: perl-XML-Parser

%description
Zimbra Connector provides access to Zimbra servers through Evolution.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%{_libdir}/evolution/%{evo_api_version}/plugins/*
%{_libdir}/evolution/*/plugins/*
#%{_libdir}/evolution-data-server-%{eds_api_version}/camel-providers/*
%{_libdir}/evolution-data-server-*/camel-providers/*
#%{_libdir}/evolution-data-server-%{eds_api_version}/extensions/*
%{_libdir}/evolution-data-server-*/extensions/*


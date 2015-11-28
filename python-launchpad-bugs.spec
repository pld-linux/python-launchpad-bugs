Summary:	Simple Python Interface to Bugs in Launchpad
Name:		python-launchpad-bugs
Version:	0.3.5
Release:	3
License:	GPL v2/LGPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.ubuntu.com/ubuntu/pool/main/p/python-launchpad-bugs/%{name}_%{version}.tar.gz
# Source0-md5:	2751fafafe83031dc7ac5df999fed134
URL:		https://launchpad.net/python-launchpad-bugs
Patch0:		%{name}-rpm.patch
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to access bug information in Launchpad.

%prep
%setup -q -n main
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%doc docs/*
%dir %{py_sitescriptdir}/launchpadbugs
%{py_sitescriptdir}/launchpadbugs/*.py[co]
%{_examplesdir}/%{name}-%{version}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/python_launchpad_bugs-*.egg-info
%endif

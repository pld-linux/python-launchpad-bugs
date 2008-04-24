Summary:	Simple Python Interface to Bugs in Launchpad
Name:		python-launchpad-bugs
Version:	0.2.30
Release:	0.1
License:	GPL v2/LGPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.ubuntu.com/ubuntu/pool/main/p/python-launchpad-bugs/%{name}_%{version}.tar.gz
# Source0-md5:	21e633b3ecb48df2171ec51a704e7362
URL:		https://launchpad.net/python-launchpad-bugs
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to access bug information in Launchpad.

%prep
%setup -q -n %{name}-0.2.29

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%doc docs/* examples
%dir %{py_sitescriptdir}/launchpadbugs
%{py_sitescriptdir}/launchpadbugs/*.py[co]

%define		module	PyRSS2Gen

Summary:	A Python library for generating RSS 2.0 feeds
Summary(pl):	Biblioteka pythonowa do generowania kana��w RSS 2.0
Name:		python-%{module}
Version:	1.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://www.dalkescientific.com/Python/%{module}-%{version}.tar.gz
# Source0-md5:	b37ed0c9cfa4438a73dbbb0207f3aff6
URL:		http://www.dalkescientific.com/Python/PyRSS2Gen.html
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python library for generating RSS 2.0 feeds.

%description -l pl
Biblioteka pythonowa s�u��ca do generowania kana��w RSS 2.0.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}.py[co]

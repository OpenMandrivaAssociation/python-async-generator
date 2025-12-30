%global pypi_name async_generator

Name:           python-async-generator
Version:        1.10
Release:        7
Summary:        Async generators and context managers for Python 3
Group:          Development/Python
License:        MIT -or- Apache License 2.0
URL:            https://github.com/python-trio/async_generator
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/async_generator-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  python%{pyver}dist(sphinxcontrib-trio)
#BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(sphinx)

%description
Async generators and context managers for Python 3

%package doc
Summary:        async-generator documentation

%description doc
Documentation for async-generator

%files
%license LICENSE.MIT LICENSE LICENSE.APACHE2
%doc README.rst
%{python_sitelib}/async_generator
%{python_sitelib}/async_generator-%{version}-py*.*.egg-info

%files doc
#doc html
%license LICENSE.MIT LICENSE LICENSE.APACHE2

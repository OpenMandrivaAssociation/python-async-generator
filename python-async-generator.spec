# Created by pyp2rpm-3.3.2
%global pypi_name async-generator

Name:           python-%{pypi_name}
Version:        1.10
Release:        2
Summary:        Async generators and context managers for Python 3
Group:          Development/Python
License:        MIT -or- Apache License 2.0
URL:            https://github.com/python-trio/async_generator
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/async_generator-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-sphinxcontrib_trio
#BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
%{?python_provide:%python_provide python-%{pypi_name}}

%description
 :target:

%package -n python-%{pypi_name}-doc
Summary:        async-generator documentation
%description -n python-%{pypi_name}-doc
Documentation for async-generator

%prep
%autosetup -n async_generator-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build
# generate html docs
#PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
%py_install

#check
#{__python} setup.py test

%files
%license LICENSE.MIT LICENSE LICENSE.APACHE2
%doc README.rst
%{python_sitelib}/async_generator
%{python_sitelib}/async_generator-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
#doc html
%license LICENSE.MIT LICENSE LICENSE.APACHE2

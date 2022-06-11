Summary:        A modernist sans serif font
Name:           tau-manrope-fonts
Version:        1
Release:        3%{?dist}
License:        OFL
URL:            https://manropefont.com/

Source0:        https://manropefont.com/manrope.zip
Source1:        README.md
Source2:        LICENSE
BuildArch:      noarch

%description
Manrope – modern geometric sans-serif, packaged for use in tauOS

This package contains the non-variable font version of the Manrope font.

%prep
%setup -c -T -D -q -a 0

%build

%install
install -d %{buildroot}%{_datadir}/fonts/OTF
install -pm 644 fonts/otf/*.otf %{buildroot}%{_datadir}/fonts/OTF/

install -pm 0644 %SOURCE1 README.md

# Install licenses
mkdir -p licenses
install -pm 0644 %SOURCE1 licenses/LICENSE

%files
%doc README.md
%doc documentation.html
%license licenses/LICENSE
%{_datadir}/fonts/OTF/*.otf

 
%changelog
* Sat May 14 2022 Jamie Murphy <jamie@fyralabs.com> - 1-1
- Fix specfile

* Sat May 14 2022 Lains <lainsce@airmail.cc> - 1-1
- Initial release

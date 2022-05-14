Version: 1
Release: 1%{?dist}
URL: http://manropefont.com/

%global	fontlicense	OFL
%global	fontfamily0	Manrope
%global	fontsummary0	Modernist sans serif font
%global	fontdescription0	%{expand:
%{common_description}
 
This package contains the non-variable font version of the Manrope font.}
 
Source0: https://manropefont.com/manrope.zip

%prep
%autosetup

%install
install -d %SOURCE0 %{_datadir}/fonts/OTF
install -pm 644 %{_datadir}/fonts/otf/*.otf %{_datadir}/fonts/OTF/
 
%changelog
* Sat May 14 2022 Lains <lainsce@airmail.cc> - 1-1
- Initial release

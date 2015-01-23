Summary:        Chromium Flash player plugin
Name:           chromium-pepper-flash
Version:        16.0.0.291
Release:        2%{?dist}

License:        Proprietary
Url:            http://www.google.com/chrome
Group:          Applications/Internet
Source0:        https://dl.google.com/linux/direct/google-chrome-stable_current_i386.rpm
Source1:        https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

BuildRequires:  rpm cpio


%description
Pepper API based Adobe Flash plugin for Google's Open Source browser Chromium.


%package -n chromium-pdf-plugin
Summary:        Chromium PDF viewer plugin
Group:          Applications/Internet

%description -n chromium-pdf-plugin
Official PDF viewer plugin for Google's Open Source browser Chromium.


%package -n chromium-widevinecdm-plugin
Summary:        Chromium Widevine CDM plugin
Group:          Applications/Internet


%description -n chromium-widevinecdm-plugin
Official Widevine CDM plugin for Google's Open Source browser Chromium.

%prep
%setup -c -T


%build
%ifarch x86_64
rpm2cpio %{SOURCE1} | cpio -idmv
%else
rpm2cpio %{SOURCE0} | cpio -idmv
%endif


%install
mkdir -p %{buildroot}%{_libdir}/chromium/PepperFlash/
install -m644 opt/google/chrome/PepperFlash/* %{buildroot}%{_libdir}/chromium/PepperFlash/ 
install -m755 opt/google/chrome/libpdf.so %{buildroot}%{_libdir}/chromium/
install -m755 opt/google/chrome/libwidevinecdm.so %{buildroot}%{_libdir}/chromium/
install -m755 opt/google/chrome/libwidevinecdmadapter.so %{buildroot}%{_libdir}/chromium/


%files
%dir %{_libdir}/chromium/
%{_libdir}/chromium/PepperFlash/


%files -n chromium-pdf-plugin
%{_libdir}/chromium/libpdf.so


%files -n chromium-widevinecdm-plugin
%{_libdir}/chromium/libwidevinecdm.so
%{_libdir}/chromium/libwidevinecdmadapter.so


%changelog
* Fri Jan 23 2015 Arkady L. Shane <ashejn@russianfedora.ru> 16.0.0.291-2.R
- added Widevine CDM plugin

* Thu Jan 22 2015 Arkady L. Shane <ashejn@russianfedora.ru> 16.0.0.291-1.R
- update to 16.0.0.291

* Tue Dec 23 2014 Arkady L. Shane <ashejn@russianfedora.ru> 16.0.0.235-1.R
- update to 16.0.0.235

* Thu Nov 20 2014 Arkady L. Shane <ashejn@russianfedora.ru> 15.0.0.223-1.R
- update to 15.0.0.223

* Wed Oct  8 2014 Arkady L. Shane <ashejn@russianfedora.ru> 15.0.0.152-1.R
- update to 15.0.0.152

* Wed Jun 11 2014 Arkady L. Shane <ashejn@russianfedora.ru> 14.0.0.177-1.R
- update to 14.0.0.177

* Wed Jun 11 2014 Arkady L. Shane <ashejn@russianfedora.ru> 14.0.0.145-1.R
- update to 14.0.0.145

* Wed Jun 11 2014 Arkady L. Shane <ashejn@russianfedora.ru> 14.0.0.125-1.R
- update to 14.0.0.125

* Wed Apr 30 2014 Arkady L. Shane <ashejn@russianfedora.ru> 13.0.0.206-1.R
- update to 13.0.0.206

* Wed Apr 23 2014 Arkady L. Shane <ashejn@russianfedora.ru> 13.0.0.182-1.R
- initial build

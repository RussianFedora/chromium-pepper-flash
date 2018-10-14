%global debug_package %{nil}
%global chromium_home chromium-browser

Summary:        Chromium Flash player plugin
Name:           chromium-pepper-flash
Version:        31.0.0.122
Release:        1%{?dist}

License:        Proprietary
Url:            http://www.google.com/chrome
Group:          Applications/Internet
Source0:        https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}/flash_player_ppapi_linux.i386.tar.gz
Source1:	https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}/flash_player_ppapi_linux.x86_64.tar.gz

BuildRequires:  rpm cpio


%description
Pepper API based Adobe Flash plugin for Google's Open Source browser Chromium.

%prep
%setup -c -T


%build
%ifarch x86_64
tar xaf %{SOURCE1}
%else
tar xaf %{SOURCE0}
%endif


%install
mkdir -p %{buildroot}%{_libdir}/%{chromium_home}/PepperFlash/
install -m644 *.so *.json %{buildroot}%{_libdir}/%{chromium_home}/PepperFlash/

%files
%dir %{_libdir}/%{chromium_home}/
%{_libdir}/%{chromium_home}/PepperFlash/


%changelog
* Sun Oct 14 2018 Arkady L. Shane <ashejn@russianfedora.pro> 31.0.0.122-1
- update to 31.0.0.122

* Sun Sep 16 2018 Arkady L. Shane <ashejn@russianfedora.pro> 31.0.0.108-1
- update to 31.0.0.108

* Tue Jul 17 2018 Arkady L. Shane <ashejn@russianfedora.pro> 30.0.0.134-1
- update to 30.0.0.134

* Wed Jun 27 2018 Arkady L. Shane <ashejn@russianfedora.pro> 30.0.0.113-1
- update to 30.0.0.113

* Tue Jun  5 2018 Arkady L. Shane <ashejn@russianfedora.pro> 29.0.0.171-1
- update to 29.0.0.171

* Sat Apr 28 2018 Arkady L. Shane <ashejn@russianfedora.pro> 29.0.0.140-1
- update to 29.0.0.140

* Wed Mar 14 2018 Arkady L. Shane <ashejn@russianfedora.pro> 29.0.0.113-1
- update to 29.0.0.113

* Wed Feb 14 2018 Arkady L. Shane <ashejn@russianfedora.pro> 28.0.0.161-1
- update to 28.0.0.161

* Mon Jan 29 2018 Arkady L. Shane <ashejn@russianfedora.pro> 28.0.0.137-1
- update to 28.0.0.137

* Fri Dec 15 2017 Arkady L. Shane <ashejn@russianfedora.pro> 28.0.0.126-1
- update to 28.0.0.126

* Wed Nov 15 2017 Arkady L. Shane <ashejn@russianfedora.pro> 27.0.0.187-1
- update to 27.0.0.187

* Fri Oct 20 2017 Arkady L. Shane <ashejn@russianfedora.pro> 27.0.0.170-1
- update to 27.0.0.170

* Fri Sep 29 2017 Arkady L. Shane <ashejn@russianfedora.pro> 27.0.0.130-1
- update to 27.0.0.130

* Mon Aug 28 2017 Arkady L. Shane <ashejn@russianfedora.pro> 26.0.0.151-1
- update to 26.0.0.151

* Mon Jul 17 2017 Arkady L. Shane <ashejn@russianfedora.pro> 26.0.0.137-1
- update to 26.0.0.137

* Tue Jun 20 2017 Arkady L. Shane <ashejn@russianfedora.pro> 26.0.0.131-1
- update to 26.0.0.131

* Wed May 31 2017 Arkady L. Shane <ashejn@russianfedora.pro> 25.0.0.171-1
- update to 25.0.0.171

* Fri May  5 2017 Arkady L. Shane <ashejn@russianfedora.ru> 25.0.0.148-1
- update to 25.0.0.148

* Wed Mar 15 2017 Arkady L. Shane <ashejn@russianfedora.ru> 25.0.0.127-1
- update to 25.0.0.127

* Fri Feb 24 2017 Arkady L. Shane <ashejn@russianfedora.ru> 24.0.0.221-1
- update to 24.0.0.221

* Fri Jan 27 2017 Arkady L. Shane <ashejn@russianfedora.ru> 24.0.0.194-1
- update to 24.0.0.194

* Thu Dec 15 2016 Arkady L. Shane <ashejn@russianfedora.ru> 24.0.0.186-1
- update to 24.0.0.186

* Mon Nov 28 2016 Arkady L. Shane <ashejn@russianfedora.ru> 23.0.0.207-3
- drop chromium-widevinecdm-plugin package as it is a part of chromium

* Sun Nov 27 2016 Arkady L. Shane <ashejn@russianfedora.ru> 23.0.0.207-2
- always push plugins to chromium-browser directory

* Mon Nov 14 2016 Arkady L. Shane <ashejn@russianfedora.ru> 23.0.0.207-1
- update to 23.0.0.207

* Sat Oct 29 2016 Arkady L. Shane <ashejn@russianfedora.ru> 23.0.0.205-1
- update to 23.0.0.205

* Mon Oct  3 2016 Arkady L. Shane <ashejn@russianfedora.ru> 23.0.0.162-2
- use chromium-browser folder for Fedora >= 25 as Russian Fedora
  does not provide chromium any more

* Tue Sep 20 2016 Arkady L. Shane <ashejn@russianfedora.ru> 23.0.0.162-1
- update to 23.0.0.162

* Mon Jul 25 2016 Arkady L. Shane <ashejn@russianfedora.ru> 22.0.0.209-2
- build 32 bit package

* Thu Jul 14 2016 Arkady L. Shane <ashejn@russianfedora.ru> 22.0.0.209-1.R
- update to 22.0.0.209

* Mon Jun 20 2016 Arkady L. Shane <ashejn@russianfedora.ru> 22.0.0.192-1.R
- update to 22.0.0.192

* Mon May 23 2016 Arkady L. Shane <ashejn@russianfedora.ru> 21.0.0.242-1.R
- update to 21.0.0.242
* Mon Apr 11 2016 Arkady L. Shane <ashejn@russianfedora.ru> 21.0.0.213-1.R
- update to 21.0.0.213

* Fri Mar 25 2016 Arkady L. Shane <ashejn@russianfedora.ru> 21.0.0.197-1.R
- update to 21.0.0.197

* Mon Mar 14 2016 Arkady L. Shane <ashejn@russianfedora.ru> 21.0.0.182-1.R
- update to 21.0.0.182
- Google provide only 64-bit version

* Wed Feb 10 2016 Arkady L. Shane <ashejn@russianfedora.ru> 20.0.0.306-1.R
- update to 20.0.0.306

* Thu Jan 21 2016 Arkady L. Shane <ashejn@russianfedora.ru> 20.0.0.286-1.R
- update to 20.0.0.286

* Sun Jan 10 2016 Arkady L. Shane <ashejn@russianfedora.ru> 20.0.0.267-1.R
- update to 20.0.0.267

* Thu Dec 10 2015 Arkady L. Shane <ashejn@russianfedora.ru> 20.0.0.228-1.R
- update to 20.0.0.228

* Thu Nov 12 2015 Arkady L. Shane <ashejn@russianfedora.ru> 19.0.0.245-1.R
- update to 19.0.0.245

* Mon Oct 26 2015 Arkady L. Shane <ashejn@russianfedora.ru> 19.0.0.226-1.R
- update to 19.0.0.226

* Thu Oct 22 2015 Arkady L. Shane <ashejn@russianfedora.ru> 19.0.0.207-1.R
- update to 19.0.0.207

* Tue Sep 29 2015 Arkady L. Shane <ashejn@russianfedora.ru> 19.0.0.185-1.R
- update to 19.0.0.185

* Wed Aug 12 2015 Arkady L. Shane <ashejn@russianfedora.ru> 18.0.0.233-1.R
- update to 18.0.0.233

* Wed Jul 15 2015 Arkady L. Shane <ashejn@russianfedora.ru> 18.0.0.209-1.R
- update to 18.0.0.209

* Thu Jul 09 2015 Arkady L. Shane <ashejn@russianfedora.ru> 18.0.0.204-1.R
- update to 18.0.0.204

* Fri Jul 03 2015 Arkady L. Shane <ashejn@russianfedora.ru> 18.0.0.194-1.R
- update to 18.0.0.194

* Sun Jun 14 2015 Arkady L. Shane <ashejn@russianfedora.ru> 18.0.0.160-1.R
- update to 18.0.0.160

* Thu May 14 2015 Arkady L. Shane <ashejn@russianfedora.ru> 17.0.0.188-1.R
- update to 17.0.0.188

* Wed Apr 15 2015 Arkady L. Shane <ashejn@russianfedora.ru> 17.0.0.169-1.R
- update to 17.0.0.169
- no more pdf plugin

* Wed Mar 18 2015 Arkady L. Shane <ashejn@russianfedora.ru> 17.0.0.134-1.R
- update to 17.0.0.134

* Tue Feb 24 2015 Arkady L. Shane <ashejn@russianfedora.ru> 16.0.0.305-1.R
- update to 16.0.0.305

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

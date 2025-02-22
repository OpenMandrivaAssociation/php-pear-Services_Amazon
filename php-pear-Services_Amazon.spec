%define		_class		Services
%define		_subclass	Amazon
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.9.0
Release:	2
Summary:	Access to Amazon.com's web services
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Services_Amazon/
Source0:	http://download.pear.php.net/package/Services_Amazon-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Services_Amazon uses Amazon.com's web services to allow developers to
search and provide associate links for specific ISBN numbers, authors,
artist, directors, and publishers among other things.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-8mdv2012.0
+ Revision: 742269
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-7
+ Revision: 679573
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-6mdv2011.0
+ Revision: 613767
- the mass rebuild of 2010.1 packages

* Tue Nov 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.0-5mdv2010.1
+ Revision: 467076
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.0-4mdv2010.0
+ Revision: 441564
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-3mdv2009.0
+ Revision: 237061
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.7.0-2mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-2mdv2008.0
+ Revision: 53923
- fix deps

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-1mdv2008.0
+ Revision: 15747
- 0.7.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdv2007.0
+ Revision: 82565
- Import php-pear-Services_Amazon

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdk
- 0.4.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1mdk
- initial Mandriva package (PLD import)



Summary:	HTX - Hypertext cross-reference utilities
Summary(pl):	HTX - narzêdzia do odsy³aczy hipertekstowych
Name:		starlink-htx
# from URL: v1.2-7 release 218
Version:	1.2_7.218
Release:	1
# according to http://www.starlink.rl.ac.uk/store/conditions.html
License:	GPL
Group:		Applications/Text
#Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/htx/htx.tar.Z
Source0:	htx.tar.Z
# Source0-md5:	cdd9c905f11bf292c81baa37f0499751
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_HTX.html
BuildArch:	noarch
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	grep
Requires(postun):	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
HTX is a set of utilities that allows you to maintain and access a
collection of dynamic multi-page hypertext documents that refer to
each other. Its main element is a hypertext linker which can be used
to establish cross-references between documents and to re-establish
these whenever changes occur to individual documents.

%description -l pl
HTX to zbiór narzêdzi pozwalaj±cych na zarz±dzanie i dostêp do
kolekcji dynamicznych wielostronnicowych dokumentów hipertekstowych
odwo³uj±cych siê do siebie nawzajem. G³ównym elementem jest linker
hipertekstowy, który mo¿e byæ u¿ywany do tworzenia odsy³aczy miêdzy
dokumentami oraz odtwarzania ich po zmianach w poszczególnych
dokumentach.

%prep
%setup -q -c

%build
# don't be afraid - it doesn't mean x86-only
SYSTEM=ix86_Linux \
./mk build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/{include,lib,share}

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if ! grep -q '^%{stardir}/share$' /etc/ld.so.conf ; then
	echo '%{stardir}/share' >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun
if [ "$1" = "0" ]; then
	umask 022
	grep -v "^%{stardir}/share$" /etc/ld.so.conf > /etc/ld.so.conf.tmp
	mv -f /etc/ld.so.conf.tmp /etc/ld.so.conf
fi
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc htx.news
# starlink software hierarchy
%dir %{stardir}
%dir %{stardir}/bin
%dir %{stardir}/dates
%docdir %{stardir}/docs
%dir %{stardir}/docs
%dir %{stardir}/include
%dir %{stardir}/help
%dir %{stardir}/lib
%dir %{stardir}/share
# package contents
%attr(755,root,root) %{stardir}/bin/findme
%attr(755,root,root) %{stardir}/bin/hlink
%attr(755,root,root) %{stardir}/bin/showme
%dir %{stardir}/bin/htx-scripts
%{stardir}/bin/htx-scripts/*.sed
%attr(755,root,root) %{stardir}/bin/htx-scripts/[!ceg]*
%attr(755,root,root) %{stardir}/bin/htx-scripts/creindex
%attr(755,root,root) %{stardir}/bin/htx-scripts/gettitle
%{stardir}/dates/*
%{stardir}/docs/sun*

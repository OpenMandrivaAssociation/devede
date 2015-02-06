Name:		devede
Version:	3.22.0
Release:	4
Summary:	Graphical frontend to create video DVDs/(S)VCDs
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.rastersoft.com/programas/devede.html
Source0:	http://www.rastersoft.com/descargas/%{name}-%{version}.tar.bz2
# Created from upstream .svg icon by GIMP - ImageMagick does not do well
# at converting .svg on the fly - AdamW 2007/09
Source1:	devede-16.png
Source2:	devede-32.png
Source3:	devede-48.png
BuildArch:	noarch
BuildRequires:	bash
BuildRequires:	coreutils
Requires:	dvdauthor
Requires:	mencoder
Requires:	mkisofs
Requires:	mplayer
Requires:	pygtk2.0
Requires:	python
Requires:	vcdimager
Requires:	python-cairo

%description
DeVeDe is a program to create video DVDs (compatible with home players) from
nearly any video format. It only uses Python, MPlayer, Mencoder, DVDAuthor,
VCDImager, and mkisofs, so it has very few dependencies.

%prep
%setup -q

# remove shebangs...
%__sed -i -e '/^#!\//, 1d' %{name}_*.py

%build
%__sed -i 's/\/usr\/lib\/devede/\/usr\/share\/devede/' %{name}

%install
# The stuff that goes to /usr/lib is just python scripts, not actually
# arch-specific. The app always looks for them in /usr/lib , even on
# x86-64. So define libdir as %_prefix/lib. See bug #31692. -AdamW 2007/06
DESTDIR=%{buildroot} \
prefix=%{_prefix} \
libdir=%{_datadir}/ \
	./install.sh

# fd.o icons
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48,scalable}/apps
mv %{buildroot}/%{_datadir}/pixmaps/%{name}.svg %{buildroot}/%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
install -m 644 %{SOURCE1} %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 644 %{SOURCE3} %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png

# redundant files, temp files...
rm -f %{buildroot}/%{_bindir}/%{name}-debug
rm -f %{buildroot}/%{_datadir}/doc/%{name}/html/*~

%find_lang %{name}

%files -f %{name}.lang
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%{_bindir}/%{name}_debug
%defattr(0644,root,root,0755)
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*


%changelog
* Fri Jul 06 2012 Guilherme Moro <guilherme@mandriva.com> 3.22.0-2mdv2012.0
+ Revision: 808405
+ rebuild (emptylog)

* Wed Jul 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.22.0-1
+ Revision: 808089
- update to 3.22.0

* Tue Jan 10 2012 Andrey Bondrov <abondrov@mandriva.org> 3.21.0-1
+ Revision: 759324
- New version 3.21.0, add clean section back for backports sake

* Sun Nov 27 2011 Alexander Khrukin <akhrukin@mandriva.org> 3.19.0-1
+ Revision: 733986
- version update 3.19.0

* Wed Oct 05 2011 Andrey Bondrov <abondrov@mandriva.org> 3.17.0-1
+ Revision: 703132
- New version: 3.17.0

* Sun Aug 22 2010 Tomas Kindl <supp@mandriva.org> 3.16.9-1mdv2011.0
+ Revision: 572052
- update to 3.16.9 (fixing #59261)
- major SPEC refactoring
- put files in their proper place, remove shebangs

* Thu Feb 25 2010 Frederik Himpe <fhimpe@mandriva.org> 3.16.4-1mdv2010.1
+ Revision: 511323
- update to new version 3.16.4

* Mon Feb 22 2010 Frederik Himpe <fhimpe@mandriva.org> 3.16.2-1mdv2010.1
+ Revision: 509656
- Update to new version 3.16.2

* Mon Feb 08 2010 Frederik Himpe <fhimpe@mandriva.org> 3.16.0-1mdv2010.1
+ Revision: 502373
- Update to new version 3.16.0

* Wed Dec 16 2009 Jérôme Brenier <incubusss@mandriva.org> 3.15.2-1mdv2010.1
+ Revision: 479615
- new version 3.15.2
- fix files list

* Mon Jul 20 2009 Frederik Himpe <fhimpe@mandriva.org> 3.14.0-1mdv2010.0
+ Revision: 398065
- update to new version 3.14.0

* Mon May 25 2009 Frederik Himpe <fhimpe@mandriva.org> 3.13.1-1mdv2010.0
+ Revision: 379658
- update to new version 3.13.1

* Fri May 15 2009 Frederik Himpe <fhimpe@mandriva.org> 3.13.0-1mdv2010.0
+ Revision: 376225
- Update to new version 3.13
- Uses gtkbuilder instead of libglade

* Thu Aug 28 2008 Frederik Himpe <fhimpe@mandriva.org> 3.11b-1mdv2009.0
+ Revision: 276947
- Update to new version 3.11b

* Tue Aug 26 2008 Frederik Himpe <fhimpe@mandriva.org> 3.11-1mdv2009.0
+ Revision: 276281
- update to new version 3.11

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 3.6-3mdv2009.0
+ Revision: 244029
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Mar 07 2008 Erwan Velu <erwan@mandriva.org> 3.6-1mdv2008.1
+ Revision: 181415
- 3.6

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 Andreas Hasenack <andreas@mandriva.com> 3.1b-2mdv2008.1
+ Revision: 108651
+ rebuild (emptylog)

* Wed Nov 14 2007 Andreas Hasenack <andreas@mandriva.com> 3.1b-1mdv2008.1
+ Revision: 108646
- added missing pygtk2.0-libglade dependency (#35532)

  + Adam Williamson <awilliamson@mandriva.org>
    - rejig icon stuff now upstream provides an svg not a png
    - requires python-cairo
    - new release 3.1b

* Mon Jul 02 2007 Adam Williamson <awilliamson@mandriva.org> 3.01-2mdv2008.0
+ Revision: 47225
- package is noarch
- install python scripts to /usr/lib even on x86-64 (fixes #31692)

* Mon Jul 02 2007 Adam Williamson <awilliamson@mandriva.org> 3.01-1mdv2008.0
+ Revision: 47189
- new release 3.01

* Sat Jun 30 2007 Adam Williamson <awilliamson@mandriva.org> 3.0-2mdv2008.0
+ Revision: 46019
- drop X-Mandriva menu category (patch1); fd.o icons

* Sat Jun 23 2007 Austin Acton <austin@mandriva.org> 3.0-1mdv2008.0
+ Revision: 43535
- new version

* Mon May 28 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 2.13-2mdv2008.0
+ Revision: 32051
- require python-psyco only in ix86

* Fri Apr 27 2007 Andreas Hasenack <andreas@mandriva.com> 2.13-1mdv2008.0
+ Revision: 18766
- Import devede


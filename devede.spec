Name:       	devede
Version:    	2.13
Release:    	%mkrel 1
Summary:    	Graphical frontend to create video DVDs
License:    	GPL
Group:      	Graphical desktop/Other
URL:        	http://www.rastersoft.com/programas/devede.html
Source:     	http://www.rastersoft.com/descargas/devede-2.13.tar.bz2
Patch:      	devede-2.13-mandriva_category.patch
BuildRoot:  	%_tmppath/%name-buildroot
BuildRequires:	bash
BuildRequires:	coreutils
Requires:   	dvdauthor
Requires:   	mencoder
Requires:   	mkisofs
Requires:   	mplayer
Requires:   	pygtk2.0
Requires:   	python
%ifarch %ix86
Requires:   	python-psyco
%endif
Requires:   	vcdimager
Requires(post,postun): desktop-common-data

%description
DeVeDe is a program to create video DVDs (compatible with home players) from
nearly any video format. It only uses Python 2.4, MPlayer, Mencoder, DVDAuthor,
VCDImager, and mkisofs, so it has very few dependencies.

%prep
%setup -q
%patch -p1 -b .mandriva_category

%build

%install
rm -rf %buildroot
DESTDIR=%buildroot \
prefix=%_prefix \
libdir=%_libdir \
	./install.sh

%find_lang %name

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(0755,root,root,0755)
%_bindir/devede
%defattr(0644,root,root,0755)
%_datadir/applications/devede.desktop
%_datadir/devede
%_datadir/doc/devede
%_datadir/pixmaps/devede.png
%_libdir/devede

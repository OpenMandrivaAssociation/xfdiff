%define name	xfdiff
%define version 4.5.0
%define release %mkrel 6

Name: 	 	%{name}
Summary: 	Graphical interface to the GNU diff and patch commands
Version: 	%{version}
Release: 	%{release}

Source:		http://downloads.sourceforge.net/xffm/%{name}-%{version}.tar.bz2
URL:		http://xffm.sf.net
License:	GPL
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	xfce-dev-tools
BuildRequires:	autoconf2.5
BuildRequires:	automake1.9
BuildRequires:	intltool
BuildRequires:	glib-gettextize
BuildRequires:	gtk2-devel
BuildRequires:	gtk-doc
BuildRequires: 	libtubo-devel

%description
Xfdiff is graphic interface to the GNU diff and patch commands. With this
utility, you can view differences side by side for files or directories.  You
can also view differences that applying a patch file would imply, without
applying the patch. You can also apply patches to the hard disc or create patch
files for differences between files or directories. All-in-all, a handy utility
for lazy chaps who don't want to type the diff command. 

%prep
%setup -q

%build
aclocal -I /usr/share/xfce4/dev-tools/m4macros -I ./m4
autoconf
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS* README*
%{_bindir}/%{name}
%{_bindir}/%{name}4
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/locale/*/*/%{name}.mo
%{_datadir}/pixmaps/%{name}-icon.png
%{_datadir}/xffm/%{name}
%{_datadir}/applications/Xfdiff.desktop



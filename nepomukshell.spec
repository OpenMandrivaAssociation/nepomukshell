Summary:	Nepomukshell
Name:		nepomukshell
Version:	0.8.0
Release:	2
Source0:	%name-%version.tar.bz2
BuildRequires:	kdelibs4-devel
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://www.kde.org
BuildRequires:	shared-desktop-ontologies

%description
Nepomukshell.

%files 
%defattr(-,root,root)
%_kde_bindir/nepomukshell
%_kde_datadir/applications/kde4/nepomukshell.desktop
%_kde_appsdir/nepomukshell
%_kde_docdir/HTML/en/nepomukshell

#-----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


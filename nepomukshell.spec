Summary:	Nepomukshell
Name:		nepomukshell
Version:	0.8.0
Release:	%mkrel 2	
Source0:	%name-%version.tar.bz2
Patch0:		nepomukshell-0.8.0-l10n-ru.patch
BuildRequires:  kdelibs4-devel
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://www.kde.org

%description
Nepomukshell

%files -f %{name}.lang
%defattr(-,root,root)
%_kde_bindir/nepomukshell
%_kde_datadir/applications/kde4/nepomukshell.desktop
%_kde_appsdir/nepomukshell

#-----------------------------------------------------------------------

%prep
%setup -q 
%patch0 -p1 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

Summary:	Serial programmer for Atmel AVR microcontrollers
Summary(pl):	Szeregowy programator dla mikrokontrolerów AVR Atmela
Name:		gAVR
Version:	0.3
Release:	1.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/gavr/%{name}-%{version}.tar.gz
# Source0-md5:	e538442a2880e6ee932068a47f865e92
Source1:	%{name}.desktop
Patch0:		%{name}-typo_fix.patch
Patch1:		%{name}-sparc.patch
URL:		http://pvdb.dse.nl/electronics/gAVR.html
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical programmer for Atmel AVR microcontrollers.

%description -l pl
Graficzny programator dla mikrokontrolerów AVR Atmela.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* .

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop

Summary:	Serial programmer for Atmel AVR microcontrollers
Summary(pl):	Szeregowy programator dla mikrokontrolerów AVR Atmela
Name:		gAVR
Version:	0.5
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/gavr/%{name}-%{version}.tar.gz
# Source0-md5:	2de5ae70ae56e015287be6b714ea5624
Source1:	%{name}.desktop
URL:		http://pvdb.dse.nl/electronics/gAVR.html
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	sed >= 4.0
ExcludeArch:	sparc sparc64 sparcv9 ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical programmer for Atmel AVR microcontrollers.

%description -l pl
Graficzny programator dla mikrokontrolerów AVR Atmela.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
sed -i -e 's#$(top_builddir)/$(MKINSTALLDIRS)#$(MKINSTALLDIRS)#' \
	po/Makefile.in.in
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop

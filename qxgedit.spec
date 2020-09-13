Name:		qxgedit
Version:	0.6.3
Release:	1
Summary:	Qt XG Editor
License:	GPLv2+
Group:		Sound/Midi
URL:		https://qxgedit.sourceforge.io/
Source0:	http://downloads.sourceforge.net/qxgedit/%{name}-%{version}.tar.gz

BuildRequires:	qt5-qttools
BuildRequires:  qt5-qtchooser
BuildRequires:	qt5-linguist
BuildRequires:	qt5-linguist-tools
BuildRequires:  qmake5
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)

%description
QXGEdit is a Qt GUI for editing MIDI System Exclusive files
for XG devices (eg. Yamaha DB50XG).

%prep
%setup -q

%build
%configure \
	--enable-debug

%make_build

%install
%make_install

# menu
desktop-file-install \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--set-key=Exec --set-value="%{name}" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_qt5_plugindir}/styles/libskulpturestyle.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_iconsdir}/*/*/*/%{name}.*
%{_mandir}/man1/%{name}*.1*

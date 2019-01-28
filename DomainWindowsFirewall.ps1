# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned 
#DNS: UDP (1:65535) / (53), TCP (1:65535) / (53)
#DFSR_RPC: TCP (49152:65535) / (49152:65535)
#FRS_RPC: TCP (49152:65535) / (49152:65535)
#Kerberos: TCP (49152:65535) / (88), UDP (49152:65535) / (88)
#Kerberos_PasswordChange: TCP (49152:65535) / (464), UDP (49152:65535) / (464)
#LDAP(TCP&UDP): TCP (1:65535) / (389), UDP (1:65535) / (389)
#LDAP_GC: TCP (49152:65535) / (3268)
#LDAPS: TCP (49152:65535) / (636)
#LDAPS_GC: TCP (49152:65535) / (3269)
#NetBIOS_DatagramService: UDP (49152:65535) / (138)
#NetBIOS_NameResolution: TCP (49152:65535) / (137), UDP (49152:65535) / (137)
#NetBIOS_SessionService: TCP (49152:65535) / (139)
#RPC_DynamicAssignment: TCP (49152:65535) / (1024:65535)
#RPC_EndpointMapper: TCP (49152:65535) / (135), UDP (49152:65535) / (135)
#RPC_LSA&SAM&Netlogon: TCP (49152:65535) / (49152:65535)
#SMB: TCP (1:65535) / (445), UDP (1:65535) / (445)
#W32Time: UDP (1:65535) / (123)

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
# NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
# DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
# WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# 88/TCP/UDP
New-NetFirewallRule -DisplayName “Domain TCP 88” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 88 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 88” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 88 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 88” -Profile Any -Direction Inbound –Protocol UDP –LocalPort 88 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 88” -Profile Any -Direction Outbound –Protocol UDP –RemotePort 88 -Action allow

# 389/TCP/UDP
New-NetFirewallRule -DisplayName “Domain TCP 389” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 389 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 389” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 389 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 389” -Profile Any -Direction Inbound –Protocol UDP –LocalPort 389 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 389” -Profile Any -Direction Outbound –Protocol UDP –RemotePort 389 -Action allow

# 636/TCP
New-NetFirewallRule -DisplayName “Domain TCP 636” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 636 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 636” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 636 -Action allow

# 3268/TCP
New-NetFirewallRule -DisplayName “Domain TCP 3268” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 3268 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 3268” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 3268 -Action allow

# 3269/TCP
New-NetFirewallRule -DisplayName “Domain TCP 3269” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 3269 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 3269” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 3269 -Action allow

# 445/TCP
New-NetFirewallRule -DisplayName “Domain TCP 445” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 445 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 445” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 445 -Action allow

# 135/TCP
New-NetFirewallRule -DisplayName “Domain TCP 135” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 135 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 135” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 135 -Action allow

# 137/UDP
New-NetFirewallRule -DisplayName “Domain UDP 137” -Profile Any -Direction Inbound –Protocol UDP –LocalPort 137 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 137” -Profile Any -Direction Outbound –Protocol UDP –RemotePort 137 -Action allow

# 138/UDP
New-NetFirewallRule -DisplayName “Domain UDP 389” -Profile Any -Direction Inbound –Protocol UDP –LocalPort 138 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 389” -Profile Any -Direction Outbound –Protocol UDP –RemotePort 138 -Action allow

# 139/TCP
New-NetFirewallRule -DisplayName “Domain TCP 139” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 139 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 139” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 139 -Action allow

# 464/TCP/UDP
New-NetFirewallRule -DisplayName “Domain TCP 464” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 464 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 464” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 464 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 464” -Profile Any -Direction Inbound –Protocol UDP –LocalPort 464 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 464” -Profile Any -Direction Outbound –Protocol UDP –RemotePort 464 -Action allow

# 123/UDP
New-NetFirewallRule -DisplayName “Domain UDP 123” -Profile Any -Direction Inbound –Protocol UDP –LocalPort 123 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 123” -Profile Any -Direction Outbound –Protocol UDP –RemotePort 123 -Action allow

# 53/TCP/UDP
New-NetFirewallRule -DisplayName “Domain TCP 53” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 53 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 53” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 53 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 53” -Profile Any -Direction Inbound –Protocol UDP –LocalPort 53 -Action allow
New-NetFirewallRule -DisplayName “Domain UDP 53” -Profile Any -Direction Outbound –Protocol UDP –RemotePort 53 -Action allow

# 49152-65535/TCP
New-NetFirewallRule -DisplayName “Domain TCP 49152-65535” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 49152-65535 -Action allow
New-NetFirewallRule -DisplayName “Domain TCP 49152-65535” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 49152-65535 -Action allow

#Opt WSUS
New-NetFirewallRule -DisplayName “WSUS TCP 8530” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 8530 -Action allow
New-NetFirewallRule -DisplayName “WSUS TCP 8530” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 8530 -Action allow
New-NetFirewallRule -DisplayName “WSUS TCP 8531” -Profile Any -Direction Inbound –Protocol TCP –LocalPort 8531 -Action allow
New-NetFirewallRule -DisplayName “WSUS TCP 8530” -Profile Any -Direction Outbound –Protocol TCP –RemotePort 8531 -Action allow

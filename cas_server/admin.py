# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License version 3 for
# more details.
#
# You should have received a copy of the GNU General Public License version 3
# along with this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# (c) 2015 Valentin Samir
"""module for the admin interface of the app"""
from django.contrib import admin
from .models import ServiceTicket, ProxyTicket, ProxyGrantingTicket, User, ServicePattern
from .models import Username, ReplaceAttributName, ReplaceAttributValue, FilterAttributValue
from .forms import TicketForm

class ServiceTicketInline(admin.TabularInline):
    """`ServiceTicket` in admin interface"""
    model = ServiceTicket
    extra = 0
    form = TicketForm
class ProxyTicketInline(admin.TabularInline):
    """`ProxyTicket` in admin interface"""
    model = ProxyTicket
    extra = 0
    form = TicketForm
class ProxyGrantingInline(admin.TabularInline):
    """`ProxyGrantingTicket` in admin interface"""
    model = ProxyGrantingTicket
    extra = 0
    form = TicketForm

class UserAdmin(admin.ModelAdmin):
    """`User` in admin interface"""
    inlines = (ServiceTicketInline, ProxyTicketInline, ProxyGrantingInline)

class UsernamesInline(admin.TabularInline):
    """`Username` in admin interface"""
    model = Username
    extra = 0
class ReplaceAttributNameInline(admin.TabularInline):
    """`ReplaceAttributName` in admin interface"""
    model = ReplaceAttributName
    extra = 0
class ReplaceAttributValueInline(admin.TabularInline):
    """`ReplaceAttributValue` in admin interface"""
    model = ReplaceAttributValue
    extra = 0
class FilterAttributValueInline(admin.TabularInline):
    """`FilterAttributValue` in admin interface"""
    model = FilterAttributValue
    extra = 0

class ServicePatternAdmin(admin.ModelAdmin):
    """`ServicePattern` in admin interface"""
    inlines = (
        UsernamesInline,
        ReplaceAttributNameInline,
        ReplaceAttributValueInline,
        FilterAttributValueInline
    )
    list_display = ('pos', 'name', 'pattern', 'proxy', 'single_log_out', 'proxy_callback', 'restrict_users')


admin.site.register(User, UserAdmin)
admin.site.register(ServicePattern, ServicePatternAdmin)

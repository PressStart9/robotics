from django.core.management.base import BaseCommand, CommandError
import warnings
import time
import datetime
import vk
import schedule
from django.utils.timezone import make_aware
from mainApps.models import Posts, Attachments



def check_news():
    warnings.filterwarnings('error', r"DateTimeField .* received a naive datetime", RuntimeWarning,
                            r'django\.db\.models\.fields')
    token = "18fb849986b3cf05ea999945fb98a2c1aaba70f6cc798047e78a062d651993497baac3a80e9f0c6749f3c"
    session = vk.Session(access_token=token)
    vk_api = vk.API(session, v='5.84')
    wall_content = vk_api.wall.get(domain='clubrotor1', count=100)['items']
    print('10')
    for cont in wall_content:
        #if cont['date'] > int(str(datetime.datetime.timestamp(Posts.objects.all().latest('posting_date').posting_date)).split('.')[0]):
            author = vk_api.groups.getById(group_ids=int(str(cont['owner_id']).replace("-", "")))[0]
            author_image = author['photo_50']
            author_name = author['name']
            posting_date = make_aware(datetime.datetime.fromtimestamp(cont['date']))
            text = cont['text']
            post_id = cont['id']
            post_main, created = Posts.objects.get_or_create(author_image=author_image, author_name=author_name,
                                                             posting_date=posting_date,
                                                             text=text, post_id=post_id)
            print('2', created)
            if cont.get('attachments') != None:
                for att in cont['attachments']:
                    type = att['type']
                    if type == 'photo':
                        preview = catt['photo']['sizes'][0]['url']
                        url = catt['photo']['sizes'][-1]['url']
                        width = catt['photo']['sizes'][-1]['width']
                        height = catt['photo']['sizes'][-1]['height']
                        attach = Attachments.objects.get_or_create(connect_post=post_main, type=type, preview=preview,
                                                                   url=url,
                                                                   width=width, height=height)
                    elif type == 'video':
                        preview = att['video']['photo_130']
                        vid = vk_api.video.get(owner_id=att['video']['owner_id'],
                                               videos=str(att['video']['owner_id']) + '_' + str(att['video']['id']))
                        url = vid['items'][0]['player']
                        width = vid['items'][0].get('width', None)
                        height = vid['items'][0].get('height', None)
                        attach = Attachments.objects.get_or_create(connect_post=post_main, type=type, preview=preview,
                                                                   url=url,
                                                                   width=width, height=height)
                    elif type == 'doc':
                        url = att['doc']['url']
                        preview = att['doc']['title']
                        attach = Attachments.objects.get_or_create(connect_post=post_main, type=type, url=url,
                                                                   preview=preview)
                    elif type == 'link':
                        print(att)
                        preview = att['link']['photo']['sizes'][0]['url']
                        height = att['link']['photo']['sizes'][0]['height']
                        width = att['link']['photo']['sizes'][0]['width']
                        url = att['link']['title'] + '@' + att['link']['url']
                        attach = Attachments.objects.get_or_create(connect_post=post_main, type=type, url=url, height=height, width=width,
                                                                   preview=preview)
                    time.sleep(1)
                    print('3')
            if cont.get('copy_history') != None:
                cont = cont['copy_history'][0]
                cauthor = vk_api.groups.getById(group_ids=int(str(cont['owner_id']).replace("-", "")))[0]
                cauthor_image = cauthor['photo_50']
                cauthor_name = cauthor['name']
                cposting_date = make_aware(datetime.datetime.fromtimestamp(cont['date']))
                ctext = cont['text']
                cpost_id = cont['id']
                post_copy, created = Posts.objects.get_or_create(main_history=post_main, author_image=cauthor_image,
                                                                 author_name=cauthor_name, posting_date=cposting_date,
                                                                 text=ctext, post_id=cpost_id)
                print('4')
                if cont.get('attachments') != None:
                    for catt in cont['attachments']:
                        ctype = catt['type']
                        if ctype == 'photo':
                            cpreview = catt['photo']['sizes'][0]['url']
                            curl = catt['photo']['sizes'][-1]['url']
                            cwidth = catt['photo']['sizes'][-1]['width']
                            cheight = catt['photo']['sizes'][-1]['height']
                            cattach = Attachments.objects.get_or_create(connect_post=post_copy, type=ctype,
                                                                        preview=cpreview,
                                                                        url=curl,
                                                                        width=cwidth, height=cheight)
                        elif ctype == 'video':
                            cpreview = catt['video']['photo_130']
                            cvid = vk_api.video.get(owner_id=catt['video']['owner_id'],
                                                    videos=str(catt['video']['owner_id']) + '_' + str(
                                                        catt['video']['id']))
                            curl = cvid['items'][0]['player']
                            cwidth = cvid['items'][0].get('width', None)
                            cheight = cvid['items'][0].get('height', None)
                            cattach = Attachments.objects.get_or_create(connect_post=post_copy, type=ctype,
                                                                        preview=cpreview,
                                                                        url=curl,
                                                                        width=cwidth, height=cheight)
                        elif ctype == 'doc':
                            curl = catt['doc']['url']
                            cpreview = catt['doc']['title']
                            cattach = Attachments.objects.get_or_create(connect_post=post_copy, type=ctype, url=curl,
                                                                        preview=cpreview)
                        elif ctype == 'link':
                            print(catt)
                            cpreview = catt['link']['photo']['sizes'][0]['url']
                            cheight = catt['link']['photo']['sizes'][0]['height']
                            cwidth = catt['link']['photo']['sizes'][0]['width']
                            curl = catt['link']['title'] + '@' + catt['link']['url']
                            cattach = Attachments.objects.get_or_create(connect_post=post_copy, type=ctype, url=curl, height=cheight, width=cwidth,
                                                                        preview=cpreview)
                        time.sleep(1)
                        print('5')
            time.sleep(1)


class Command(BaseCommand):
    def schedule(self):
        schedule.every(10).minutes.do(check_news)

        while 1:
            schedule.run_pending()
            time.sleep(1)

    def handle(self, *args, **options):
        self.schedule()

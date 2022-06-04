
from re import X
from twisted.internet import reactor
from scrapy import signals

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
import scrapy
import sqlite3
item={}
conn=sqlite3.connect('mydata.db')
curr=conn.cursor()
curr.execute("""DROP TABLE IF EXISTS data_tb""")
curr.execute("""create table  data_tb(Title text NOT NULL DEFAULT 'null',Rating text NOT NULL DEFAULT 'null',Seller_Name text,Seller_Rating text,Contact_Number text)""")
conn.commit()      
  


class Pythonspider(scrapy.spiders.Spider):
    
    print('5')
    name = 'tech'
        
    
     
    #url=dd[0]   
    allowed_domains = ['www.flipkart.com','dir.indiamart.com']
    #start_urls=[dd[0]]
    url="https://www.flipkart.com/mens-footwear/pr?sid=osp,cil&otracker=nmenu_sub_Men_0_Footwear&fm=neo%2Fmerchandising&iid=M_c78b2172-825e-4307-b48e-0a7db344b266_1_372UD5BXDFYS_MC.PR9Y9GHWCY6G&otracker=hp_rich_navigation_5_1.navigationCard.RICH_NAVIGATION_Fashion~Men%2BFootwear_PR9Y9GHWCY6G&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L1_view-all&cid=PR9Y9GHWCY6G"

    category=url
    def start_requests(self):
        yield scrapy.Request(self.category)
    


    def parse(self,response):
        print('7')
        c=response.css('._2UzuFa ::attr(href)').getall()
        #print(c)
        
        
        for i in c:
         #print('8')
         
         i=response.urljoin(i)
         yield scrapy.Request(i,self.parse_content)
        #self.parse_content()
         
           

    def parse_content(self,response):
        
    #q=[]
        #print('9')
        #ittem = {}
        
        
        Title=response.css('.B_NuCI::text').extract()
        #Price=response.css('._25b18c ::text').extract()
        Rating=response.css('._3LWZlK._138NNC ::text').extract()
        Seller =response.css('#sellerName span ::text').extract()
        
        item['title']= Title
        item['rating']= Rating
        item['seller_name']=Seller[0]
        item['seller_rating']=Seller[1]
        
        
        #curr.execute("""INSERT INTO data_tb(Title,Rating,Seller_Name,Seller_Rating) VALUES(?,?,?,?)""",( str(item['title']),str(item['rating']),str(item['seller_name']),str(item['seller_rating'])))
        #conn.commit()
        x="https://dir.indiamart.com/search.mp?ss="+f'{Seller[0]}'
        print(x)
        x=response.urljoin(x)
        yield scrapy.Request(x,self.contact) 
       # print(item['Contact_Number'])

    def contact(self,response):

        Contact_Number=response.css('.pns_h.duet.fwb ::text').get()
        item['Contact_Number']=Contact_Number
        #print(Contact_Number)
        
        curr.execute("""INSERT INTO data_tb(Title,Rating,Seller_Name,Seller_Rating,Contact_Number) VALUES(?,?,?,?,?)""",( str(item['title']),str(item['rating']),str(item['seller_name']),str(item['seller_rating']),str(item['Contact_Number'])))
        conn.commit()

        
        
        
        
                     
from scrapy.utils.log import configure_logging



def run_spider():
   
   
   
    configure_logging()
    runner=CrawlerRunner()
    runner.crawl(Pythonspider)

   
    d=runner.join()
    
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
run_spider()
{"filter":false,"title":"models.py","tooltip":"/accounts/models.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":26},"action":"remove","lines":["from django.db import models","","# Create your models here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":12,"column":8},"action":"insert","lines":["from django.db import models","","# Create your models here.","class Item(models.Model):","    company_name = models.CharField(max_length=100, blank=False)","    company_manager = models.CharField(max_length=50, blank=False)","    Feedback = models.TextField(max_length=200, blank=False)","    date = models.DateField()","    ","    ","    def __str__(self):","        return self.company_name","        "]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["F"],"id":3}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["f"],"id":4}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":12},"action":"remove","lines":["company_"],"id":5}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":12},"action":"remove","lines":["company_"],"id":6}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":8},"action":"remove","lines":["name"],"id":7},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["c"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["o"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["m"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["p"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["a"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["n"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["y"],"id":8},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"remove","lines":["n"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"remove","lines":["a"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["p"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"remove","lines":["m"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":["o"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["b"],"id":9},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["u"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["s"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["i"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["n"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["e"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["s"]},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":20},"end":{"row":11,"column":32},"action":"remove","lines":["company_name"],"id":10},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["b"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["u"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["s"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["i"]},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"insert","lines":["n"]},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["e"]},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["s"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":0},"end":{"row":13,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1570996370360,"hash":"b6340fea4f29b5f17f87c03fba59c39412e263b7"}
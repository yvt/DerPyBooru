class Search(object):
  def __init__(self, q=[], page=1, comments=False, fav=False, key=""):
    self.q = q
    self.page = page
    self.comments = comments
    self.fav = fav
    self.key = key

  @property
  def hostname(self):
    return("https://derpiboo.ru")

  @property
  def q(self):
    return(self.__q)

  @q.setter
  def q(self, q=[]):
    if not isinstance(q, list):
      raise TypeError("tags must be a list of strings")

    for tag in q:
      if not isinstance(tag, str):
        raise TypeError("{0} is not a string".format(tag))

      if tag == "":
        raise ValueError("empty strings aren't valid tags")

    self.__q = q

  @property
  def page(self):
    return(self.__page)

  @page.setter
  def page(self, page=1):
    if not isinstance(page, int):
      raise TypeError("page number must be an int")

    if page < 1:
      raise ValueError("page number must be greater than 1")

    self.__page = page

  @property
  def comments(self):
    return(self.__comments)

  @comments.setter
  def comments(self, comments=True):
    if not isinstance(comments, bool):
      raise TypeError("comments must be either True or False")

    self.__comments = comments

  @property
  def key(self):
    return(self.__key)

  @key.setter
  def key(self, key=""):
    if not isinstance(key, str):
      raise TypeError("key must be a string") 

    self.__key = key

  @property
  def fav(self):
    if not isinstance(fav, bool):
      raise TypeError("favorites must be either True or False")

    return(self.__fav)

  @fav.setter
  def fav(self, fav=True):
    self.__fav = fav

  @property
  def parameters(self):
    parameters = {
      "q": self.q,
      "page": self.page,
      "comments": self.comments,
      "fav": self.fav,
      "key": self.key
    }

    return(parameters)


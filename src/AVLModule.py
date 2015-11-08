class AVL :

  root = None
  countNode = 0
  typeTree = None

  def __init__(self, item='empty', parent=None) :
    self.balanceFactor = 0
    self.subroot       = item
    self.left          = None
    self.right         = None
    self.parent        = parent
    if self.root != 'empty' :
      AVL.countNode += 1
    if AVL.countNode == 1 :
      AVL.root     = self
      AVL.typeTree = type(AVL.root.subroot)

  def insert(self, newItem) :
    if type(newItem) == AVL.typeTree :
      current = AVL.root
      while True :
        if newItem < current.subroot :
          if current.left == None :
            current.left = AVL(newItem, current)
            self.__setBalanceFactor(current.left)
            break
          else :
            current = current.left
        else :
          if current.right == None :
            current.right = AVL(newItem, current)
            self.__setBalanceFactor(current.right)
            break
          else :
            current = current.right
    else : print('error')

  def __setBalanceFactor(self, current) :
    if current.balanceFactor > 1 or current.balanceFactor < -1 :
      AVL.rebalance(current)
      return
    if current.parent != None :
      if current.parent.left == current :
        current.parent.balanceFactor += 1
      elif current.parent.right == current :
        current.parent.balanceFactor -= 1
      if current.parent.balanceFactor != 0 :
        self.__setBalanceFactor(current.parent)
  @staticmethod
  def rebalance(node) :
    if node.balanceFactor < 0 :
      if node.right.balanceFactor > 0 :
        node.__rotateRight(node.right)
        node.__rotateLeft(node)
      else :
        node.__rotateLeft(node)
    elif node.balanceFactor > 0 :
      if node.left.balanceFactor < 0 :
        node.__rotateLeft(node.left)
        node.__rotateRight(node)
      else :
        node.__rotateLeft(node)
  def __rotateLeft(self, oldRoot) :
    # правый потомок старого корня поддерева становиться новым корнем #
    # старый корень становиться левым потомком нового корня           #
    # если у нового корня есть левый потомок, то он станет правым     #
    # потомком старого корня. уфф...                                  #
    newRoot       = oldRoot.right
    oldRoot.right = newRoot.left
    if newRoot.left != None :
      newRoot.left.parent = oldRoot
    newRoot.parent = oldRoot.parent
    # теперь нужно связать либо левый,                            #
    # либо правый указатель родителя старого корня с новым корнем #
    # но если тот был корнем всего дерева, то изменить AVL.root   #
    if AVL.root == oldRoot :
      AVL.root = newRoot
      newRoot.parent = None
    else :
      if oldRoot.parent.left == oldRoot :
        oldRoot.parent.left = newRoot
      else :
        oldRoot.parent.right = newRoot
    # родителем старого корня становться новый корень #
    newRoot.left = oldRoot
    oldRoot.parent = newRoot
    # новые значения факторов баланса #
    oldRoot.balanceFactor = (oldRoot.balanceFactor + 1 -\
                                min(newRoot.balanceFactor, 0))%2
    newRoot.balanceFactor = (newRoot.balanceFactor + 1 -\
                                max(oldRoot.balanceFactor, 0))%2
  # зеркально к левому повороту #
  def __rotateRight(self, oldRoot) :
    newRoot = oldRoot.left
    oldRoot.left = newRoot.right
    # если у нового корня есть правый потомок #
    # сделать его родителем старый корень     #
    if newRoot.right != None :
      newRoot.right.parent = oldRoot
    newRoot.parent = oldRoot.parent
    if AVL.root == oldRoot :
      AVL.root = newRoot
      newRoot.parent = None
    else :
      if oldRoot.parent.left == oldRoot :
        oldRoot.parent.left = newRoot
      else :
        oldRoot.parent.right = newRoot
    newRoot.right = oldRoot
    oldRoot.parent = newRoot
    oldRoot.balanceFactor = (oldRoot.balanceFactor + 1 -\
                                min(newRoot.balanceFactor, 0))%2
    newRoot.balanceFactor = (newRoot.balanceFactor + 1 -\
                                max(oldRoot.balanceFactor, 0))%2
  def search(self, key) :
    current = AVL.root
    while True :
      if key < current.subroot :
        if current.left != None :
          current = current.left
          h += 1
        else : return None
      elif key > current.item :
        if current.right != None :
          current = current.right
          h += 1
        else : return None
      elif key == current.item :
        return current.root, current

  @staticmethod
  def inorder(tree) :
    if tree :
      AVL.inorder(tree.left)
      print(repr((tree.subroot, tree.balanceFactor)), end=' ')
      AVL.inorder(tree.right)
  @staticmethod
  def preorder(tree) :
    if tree :
      print(repr((tree.subroot, tree.balanceFactor)), end=' ')
      AVL.preorder(tree.left)
      AVL.preorder(tree.right)
  @staticmethod
  def postorder(tree) :
    if tree :
      AVL.postorder(tree.left)
      AVL.postorder(tree.right)
      print(repr((tree.subroot, tree.balanceFactor)), end=' ')


from Components.PerspectiveComponents.Displays.Tree import Tree


class ProgressiveTree(Tree):

    def __init__(self, locator, driver):
        Tree.__init__(self, locator=locator, driver=driver)


    def expand_item_path(self, item_path):

        pass

    
    def is_item_path_expanded(self, item_path):

        pass
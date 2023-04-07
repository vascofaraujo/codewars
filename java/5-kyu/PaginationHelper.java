import java.util.*;

// TODO: complete this object/class

public class PaginationHelper<I> {

    /**
     * The constructor takes in an array of items and a integer indicating how many
     * items fit within a single page
     */
    public PaginationHelper(List<I> collection, int itemsPerPage) {
        System.out.println(collection);

        int numPages = (int) Math.ceil(collection.size() /(double) itemsPerPage);
        System.out.println(numPages);
        List<I>[] page = new ArrayList[numPages];
        int i = 0;
        int first = 0;
        int last = itemsPerPage;
        while (numPages > 0){
            
            page[i].add(collection.subList(first, last));
            first = first + itemsPerPage;
            if ((last + itemsPerPage) > collection.size()){
                last = collection.size();
            }else{
                last = last + itemsPerPage;
            }
            numPages--;

        }

        System.out.println(page);
    }
    
    /**
     * returns the number of items within the entire collection
     */
    public int itemCount() {
        return 0;
    }
    
    /**
     * returns the number of pages
     */
    public int pageCount() {
        return 0;
    }
    
    /**
     * returns the number of items on the current page. page_index is zero based.
     * this method should return -1 for pageIndex values that are out of range
     */
    public int pageItemCount(int pageIndex) {
        return 0;
    }
    
    /**
     * determines what page an item is on. Zero based indexes
     * this method should return -1 for itemIndex values that are out of range
     */
    public int pageIndex(int itemIndex) {
        return 0;
    }

    public static void main(String[] args) {
        PaginationHelper<Character> helper = new PaginationHelper(Arrays.asList('a', 'b', 'c', 'd', 'e', 'f'), 4);
        helper.pageCount(); //should == 2
        helper.itemCount(); //should == 6
        helper.pageItemCount(0); //should == 4
        helper.pageItemCount(1); // last page - should == 2
        helper.pageItemCount(2); // should == -1 since the page is invalid

    }
    
}

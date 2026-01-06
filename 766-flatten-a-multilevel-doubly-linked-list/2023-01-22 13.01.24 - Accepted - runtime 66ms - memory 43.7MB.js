/**
 * // Definition for a Node.
 * function Node(val,prev,next,child) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 *    this.child = child;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var flatten = function(head) {
    let currentNode = head;
    while (currentNode) {
        if (currentNode.child) {
            let endNode = currentNode.next;
            let childNode = currentNode.child;
            currentNode.next = childNode;
            childNode.prev = currentNode;
            currentNode.child = null;
            let childNodeTail = flattenHelper(childNode)
            childNodeTail.next = endNode;
            if (endNode) {
                endNode.prev = childNodeTail;
            }
        }
        currentNode = currentNode.next;
    }
    return head;
};

var flattenHelper = function(currentNode) {
    let n = currentNode;
    while (n.next) {
        n = n.next
    }
    return n
}
// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

class Node {
	constructor(x, l = null, r = null) {
		this.x = x;
		this.l = l;
		this.r = r;
 	}
}

class Tree {
	constructor() {
		this.root = null;
 	}
	add(n, prev_n) {
        let x = n.x;
        let l = n.l;
        let r = n.r;
        if (this.root == null) {
            this.root = new Node(x);
            prev_n = this.root;
        }
        if (l == null) {
            prev_n.l = null;
        }
        else {
            prev_n.l = l;
            this.add(l, prev_n.l);
        }
        if (r == null) {
            prev_n.r = null;
        }
        else {
            prev_n.r = r;
            this.add(r, prev_n.r);
        }
    }
    inorder(node = this.root) {
        if (!node) {
            return;
        }
        this.inorder(node.l);
        console.log(node.x);
        this.inorder(node.r);
    }
}

class Zigzag {
    constructor() {
		this.maxStep = 0;
 	}

    find_longest_zigzag(tree) {
        this.maxStep = 0;
        this.dfs(tree.root, true, 0);
        this.dfs(tree.root, false, 0);
        return this.maxStep;
    }
    dfs(root, isLeft, step) {
        if (root == null) return;
        // console.log(root.x, isLeft, step);
        // if (root.l != null) console.log("left: ", root.l.x);
        // if (root.r != null) console.log("right: ", root.r.x);
        // console.log("-----");
        this.maxStep = Math.max(this.maxStep, step); // update max step sofar

        if (isLeft) {
            this.dfs(root.l, true, 0); // keep going from root to left
            this.dfs(root.r, false, step + 1); // restart going from root to right
        } else {
            this.dfs(root.r, false, 0); // keep going from root to right
            this.dfs(root.l, true, step + 1); // restart going from root to left
        }
    }

}

function solution(T) {
    // write your code in JavaScript (Node.js 8.9.4)
    // console.log(T);
    let tree = new Tree();
    tree.add(T, null);
    // tree.inorder();
    // console.log(tree.root);
        
    let zigzag = new Zigzag();
    return zigzag.find_longest_zigzag(tree);
}

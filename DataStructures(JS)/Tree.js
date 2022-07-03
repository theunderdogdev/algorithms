class Node {
	constructor(data) {
		this.data = data;
		this.left = undefined;
		this.right = undefined;
	}
}

const Queue = {
	storage: [],
	/**
	 *
	 * @param {any} data
	 */
	enqueue(data) {
		this.storage.push(data);
	},
	/**
	 *
	 * @returns {any}
	 */
	dequeue() {
		const data = this.storage[0];
		this.storage.splice(0, 1);
		return data;
	},
	length() {
		return this.storage.length;
	},
};

const BST = {
	/**
	 *
	 * @param {Number} data
	 */
	init(data) {
		this.root = new Node(data);
		this.root;
		this.rootIndex = 0;
	},
	inf: Infinity,
	/**
	 * Builds a binary search tree and returns the tree built so far
	 * @param {Node} node
	 * @param {Number} data
	 * @returns {Node}
	 */
	buildTree(node, data) {
		if (node == undefined) {
			return new Node(data);
		} else {
			if (data < node.data) {
				node.left = this.buildTree(node.left, data);
			} else {
				node.right = this.buildTree(node.right, data);
			}
			return node;
		}
	},
	/**
	 * Returns preorder traversal of a binary tree
	 * Takes root and an empty array as its parameters
	 * @param {Node} node
	 * @param {Array} preOrderArray
	 * @returns
	 */
	preOrder(node, preOrderArray) {
		if (node == undefined) {
			return;
		}
		preOrderArray.push(node.data);
		this.preOrder(node.left, preOrderArray);
		this.preOrder(node.right, preOrderArray);
		return preOrderArray;
	},
	/**
	 * Returns inorder traversal of a binary tree
	 * Takes root and an empty array as its parameters
	 * @param {Node} node
	 * @param {Array} inOrderArray
	 * @returns
	 */
	inOrder(node, inOrderArray) {
		if (node == undefined) {
			return;
		}
		this.inOrder(node.left, inOrderArray);
		inOrderArray.push(node.data);
		this.inOrder(node.right, inOrderArray);
		return inOrderArray;
	},
	/**
	 * Returns postorder traversal of a binary tree
	 * Takes root and an empty array as its parameters
	 * @param {Node} node
	 * @param {Array} postOrderArray
	 * @returns
	 */
	postOrder(node, postOrderArray) {
		if (node == undefined) {
			return;
		}
		this.inOrder(node.left, postOrderArray);
		this.inOrder(node.right, postOrderArray);
		postOrderArray.push(node.data);
		return postOrderArray;
	},
	/**
	 * Returns maximum of the tree/subtree
	 * @param {Node} node
	 * @returns {Node}
	 */
	maxNodeFinder(node) {
		if (node.right == undefined) {
			return node;
		}
		return this.maxNodeFinder(node.right);
	},
	/**
	 * Returns minium of the tree/subtree
	 * @param {Node} node
	 * @returns {Node}
	 */

	minNodeFinder(node) {
		if (node.left == undefined) {
			return node;
		}
		return this.minNodeFinder(node.left);
	},
	/**
	 * Checks if a binary tree is a Binary Search Tree by validating
	 *  if it's right and left descendants are less than or greater
	 * than its antecedants to the left and right respectively
	 * @param {Node} node
	 * @returns {Boolean}
	 */

	isBSTree(node) {
		if (node == undefined) {
			return true;
		}
		if (node.left != undefined && this.maxNodeFinder(node.left) > node.data) {
			return false;
		}
		if (node.right != undefined && this.minNodeFinder(node.right) < node.data) {
			return false;
		}
		if (!this.isBSTree(node.left) || !this.isBSTree(node.right)) {
			return false;
		}
		return true;
	},
	/**
	 * Returns the depth of binary tree
	 * @param {Node} node
	 * @returns {Number}
	 */
	treeDepth(node) {
		if (node == undefined) {
			return 0;
		} else {
			return (
				1 + Math.max(this.treeDepth(node.left), this.treeDepth(node.right))
			);
		}
	},
	/**
	 * Checks if a binary tree is a Binary Search Tree using limits given
	 * Call the function by passing Infinity and Root as your default argument
	 * returns true or false depending on the condition
	 * @param {Node} node
	 * @param {Number} min_val
	 * @param {Number} max_val
	 * @returns {boolean}
	 */
	isBSTreeLimits(node, min_val, max_val) {
		if (node == undefined) {
			return true;
		} else if (node.data < min_val || node.data > max_val) {
			return false;
		} else {
			return (
				this.isBSTreeLimits(node.left, min_val, node.data) &&
				this.isBSTreeLimits(node.right, node.data, max_val)
			);
		}
	},
	/**
	 * Takes root node and an array to store traversal data
	 * returns the level order traversal of a binary tree
	 * @param {Node} node
	 * @param {Arrray} orderArr
	 * @returns {Array}
	 */
	bFTraversal(node, orderArr) {
		if (node == undefined) return;
		const queue = Object(Queue);
		console.log(queue);
		queue.enqueue(node);
		while (queue.length() > 0) {
			const current = queue.dequeue();
			orderArr.push(current.data);
			if (current.left !== undefined) {
				queue.enqueue(current.left);
			}
			// If current has a right child node, add it to the queue.
			if (current.right !== undefined) {
				queue.enqueue(current.right);
			}
		}
		return orderArr;
	},
	flattenTree(node) {
		if (node == undefined) {
			return;
		}
		if (node.left == undefined && node.right == undefined) {
			return;
		}
		if (node.left != undefined) {
			this.flattenTree(node.left);
			let temp = node.right;
			node.right = node.left;
			node.left = undefined;
			let currentRight = node.right;
			while (currentRight.right != undefined) {
				currentRight = currentRight.right;
			}
			currentRight.right = temp;
		}
		this.flattenTree(node.right);
	},
	/**
	 * Takes inorder and preorder traversals of a tree and builds a binary tree
	 *
	 * @param {Array} inArray
	 * @param {Array} preArray
	 * @param {Number} start
	 * @param {Number} end
	 * @returns {Node}
	 */
	buildTreeByOrders(inArray, preArray, start, end) {
		this.rootIndex = 0;
		return this._buildTree(inArray, preArray, start, end);
	},
	/**
	 *
	 * Call to this function without resetting index is prohitbited
	 * Either call this function by setting the BST.rootIndex to zero
	 * or call BST.buildTreeByOrders function instead
	 */
	_buildTree(inArray, preArray, start, end) {
		if (start > end) {
			return;
		}
		const rootNode = new Node(preArray[this.rootIndex++]);
		if (start == end) {
			return rootNode;
		}
		const inOrderRootIndex = inArray.indexOf(rootNode.data);
		rootNode.left = this._buildTree(
			inArray,
			preArray,
			start,
			inOrderRootIndex - 1
		);
		rootNode.right = this._buildTree(
			inArray,
			preArray,
			inOrderRootIndex + 1,
			end
		);
		return rootNode;
	},
	/**
	 * Builds a random binary tree with the given data
	 * No convention just randomly subceeded down the root
	 * @param {Node} root
	 * @param {Number} data
	 * @returns {Node}
	 */
	buildRandomTree(node, data) {
		if (node == undefined) {
			return new Node(data);
		} else {
			const random = Math.round(Math.random()) * 1;
			if (random == 0) {
				node.left = this.buildRandomTree(node.left, data);
			} else {
				node.right = this.buildRandomTree(node.right, data);
			}
			return node;
		}
	},
	deleteNode(node, key) {
		if (node == undefined) {
			return node;
		}
		if (key < node.data) {
			node.left = this.deleteNode(node.left, key);
		} else if (key > node.data) {
			node.right = this.deleteNode(node.right, key);
		} else {
			if (node.left == undefined) {
				return node.right;
			} else if (node.right == undefined) {
				return node.left;
			}
			node.data = this.minNodeFinder(node.right).data;
			node.right = this.deleteNode(node.right, node.data);
		}
		return node;
	},
	describe() {
		console.log(this);
	},
};
/* 
Logic to delete node is 
if root->left and root->right is null 
 */
const dryRun = () => {
	const arr = [
		17, 44, 90, 47, 80, 53, 43, 1, 55, 82, 62, 11, 4, 54, 63, 9, 5, 40, 6, 68,
		94, 86, 66, 96,
	];

	BST.init(50);
	arr.forEach((el) => {
		BST.buildTree(BST.root, el);
	});

	BST.describe();
	console.log(BST.treeDepth(BST.root));
};

module.exports = BST;
module.exports.Node = Node;
module.exports.dryRun = dryRun;
/*	
     
// New lines
give three nodes in how many ways we can arrange them
 2n
   C
    n
---------
(n + 1)

  */

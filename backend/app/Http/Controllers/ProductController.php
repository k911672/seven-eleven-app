<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Product;

class ProductController extends Controller
{
    public function index() {
        $items[] = Product::where('category', "弁当")->random(1);
        $items[] = Product::where('category', "カフェ")->random(1);
        $items[] = Product::where('category', "サラダ")->random(1);

        return response()->json(['res' => 'OK', "items" => $items]);
    }
}

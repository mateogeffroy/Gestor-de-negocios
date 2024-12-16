import React from "react";

function NavBar() {
    return (
        <nav>
            <ul className="flex space-x-4">
                <li><a href="/" className="font-nunito">Inicio</a></li>
                <li><a href="/productos" className="font-nunito">Productos</a></li>
            </ul>
        </nav>
    );
}

export default NavBar;
